# plik: pomiary/views.py
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from .models import GridParamValuesDic, SensorParamDic, SensorData, GAoi, \
    SensorSensors, GridParamValues
from django.db.models import Field, Transform, Max
import json
from datetime import datetime, timedelta
import csv
from .middleware import SchemaMiddleware


class CastToNumeric(Transform):
    lookup_name = 'cast_numeric';
    function = 'CAST';
    template = '%(function)s(%(expressions)s AS numeric)'


Field.register_lookup(CastToNumeric)


def get_sensor_table_data(request):
    serial_number = request.GET.get('serial_number')
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')
    as_csv = request.GET.get('format') == 'csv'
    param_codes = request.GET.getlist('param_codes[]')

    if not all([serial_number, start_date, end_date]):
        return JsonResponse({'error': 'Missing serial number or date range'}, status=400)

    if as_csv:
        all_sensor_data = SensorData.objects.filter(
            sensor_serial_num__serial_number=serial_number,
            time_stamp__range=(start_date, end_date)
        ).order_by('time_stamp').select_related('param', 'sensor_serial_num')

        if param_codes:
            all_sensor_data = all_sensor_data.filter(param__parameter_cd__in=param_codes)

        response = HttpResponse(content_type='text/csv')
        response[
            'Content-Disposition'] = f'attachment; filename="sensor_{serial_number}_{start_date}_to_{end_date}.csv"'
        writer = csv.writer(response)

        writer.writerow(['Sensor Name', 'Parameter', 'Timestamp', 'Value', 'Unit'])

        for item in all_sensor_data:
            writer.writerow([
                item.sensor_serial_num.name,
                item.param.parameter_description,
                item.time_stamp.strftime('%Y-%m-%d %H:%M:%S'),
                item.data,
                item.param.unit
            ])

        return response

    if not param_codes:
        return JsonResponse({'error': 'Missing parameter codes for table view'}, status=400)

    data_query = SensorData.objects.filter(
        sensor_serial_num__serial_number=serial_number,
        time_stamp__range=(start_date, end_date),
        param__parameter_cd__in=param_codes
    ).order_by('time_stamp').select_related('param', 'sensor_serial_num')

    param_description = ""
    param_unit = ""
    if param_codes:
        try:
            param_info = SensorParamDic.objects.get(parameter_cd=param_codes[0])
            param_description = param_info.parameter_description
            param_unit = param_info.unit
        except SensorParamDic.DoesNotExist:
            pass

    table_data = list(data_query.values('sensor_serial_num__name', 'time_stamp', 'data'))
    for row in table_data:
        row['time_stamp'] = row['time_stamp'].strftime('%Y-%m-%d %H:%M:%S')

    return JsonResponse({'table_data': table_data, 'param_description': param_description, 'param_unit': param_unit},
                        safe=False)


def get_param_values(request, param_code):
    values = GridParamValuesDic.objects.filter(param_code=param_code).values('value_code', 'value_name').order_by(
        'value_name')
    return JsonResponse(list(values), safe=False)


def get_chart_data(request):
    param_codes = request.GET.getlist('sensor_params[]')
    start_date_str = request.GET.get('start_date')
    end_date_str = request.GET.get('end_date')
    serial_number = request.GET.get('serial_number', None)

    if not all([param_codes, start_date_str, end_date_str]):
        return JsonResponse({'error': 'Missing parameters'}, status=400)

    start_date = datetime.fromisoformat(start_date_str)
    end_date = datetime.fromisoformat(end_date_str)

    query = SensorData.objects.filter(
        param__parameter_cd__in=param_codes,
        time_stamp__range=(start_date, end_date)
    ).order_by('time_stamp').select_related('param', 'sensor_serial_num', 'sensor_serial_num__hardware')

    if serial_number:
        query = query.filter(sensor_serial_num__serial_number=serial_number)

    #DATA_LIMIT = 100000
    sensor_data = query#[:DATA_LIMIT]

    used_sensors_info = {}

    grouped_data = {}

    for item in sensor_data:
        if not item.sensor_serial_num or not item.param:
            continue

        sensor_serial = item.sensor_serial_num.serial_number
        param_code = item.param.parameter_cd
        key = (param_code, sensor_serial)

        if key not in grouped_data:
            grouped_data[key] = []
        grouped_data[key].append({'x': item.time_stamp.isoformat(), 'y': item.data})

        sensor = item.sensor_serial_num
        if sensor and sensor.hardware and sensor.serial_number not in used_sensors_info:
            lat_str = sensor.latitude.replace(',', '.') if sensor.latitude else None
            lon_str = sensor.longitude.replace(',', '.') if sensor.longitude else None
            used_sensors_info[sensor.serial_number] = {'model': sensor.hardware.model,
                                                       'description': sensor.hardware.description, 'lat': lat_str,
                                                       'lon': lon_str, 'serial_number': sensor.serial_number,
                                                       'name': sensor.name}

    datasets = []
    param_infos = {p.parameter_cd: p for p in SensorParamDic.objects.filter(parameter_cd__in=param_codes)}

    for (param_code, sensor_serial), data_points in grouped_data.items():
        param_info = param_infos.get(param_code)
        sensor_info = used_sensors_info.get(sensor_serial)

        if param_info and sensor_info:
            dataset_label = f"{sensor_info['name']}: {param_info.parameter_description} ({param_info.unit})"
        elif param_info:
            dataset_label = f"{sensor_serial}: {param_info.parameter_description} ({param_info.unit})"
        else:
            dataset_label = f"{sensor_serial}: {param_code}"

        datasets.append({
            'label': dataset_label,
            'data': data_points,
            'sensor_serial': sensor_serial,
            'param_code': param_code
        })

    return JsonResponse({'datasets': datasets, 'used_sensors': list(used_sensors_info.values())})


def panel_glowny(request):
    selected_schema = request.GET.get('schema', SchemaMiddleware.DEFAULT_SCHEMA)
    if selected_schema not in SchemaMiddleware.AVAILABLE_SCHEMAS:
        selected_schema = SchemaMiddleware.DEFAULT_SCHEMA

    sensor_params = SensorParamDic.objects.all().order_by('parameter_description')
    aoi_geojson = {}
    try:
        aoi_object = GAoi.objects.first()
        if aoi_object and aoi_object.geom:
            aoi_object.geom.srid = 2180
            aoi_object.geom.transform(4326)
            features = [{"type": "Feature", "geometry": json.loads(aoi_object.geom.geojson),
                         "properties": {"name": "Area of Interest"}}]
            aoi_geojson = {"type": "FeatureCollection", "features": features}
    except Exception as e:
        print(f"Error processing AOI polygon in Python: {e}")

    schema_bounds = {
        'daleszyce': {
            'southWest': [50.81, 20.702718],
            'northEast': [50.770404, 20.766823]
        },
        'gosciecice': {
            'southWest': [50.72, 17.06],
            'northEast': [50.76, 17.12]
        }
    }

    today = datetime.now()
    end_date_val_default = today.strftime('%Y-%m-%d')

    latest_date_info = SensorData.objects.aggregate(latest_date=Max('time_stamp'))
    latest_date = latest_date_info.get('latest_date')

    if latest_date:
        start_date_default = (latest_date.date() - timedelta(days=30)).strftime('%Y-%m-%d')
    else:
        start_date_default = (today - timedelta(days=30)).strftime('%Y-%m-%d')

    start_date_val = request.GET.get('start_date', start_date_default)
    end_date_val = request.GET.get('end_date', end_date_val_default)

    context = {
        'aoi_geojson': aoi_geojson,
        'sensor_params': sensor_params,
        'available_schemas': SchemaMiddleware.AVAILABLE_SCHEMAS,
        'selected_schema': selected_schema,
        'start_date_val': start_date_val,
        'end_date_val': end_date_val,
        'schema_bounds': schema_bounds,
    }
    return render(request, 'pomiary/panel.html', context)