from django.urls import path
from . import views

urlpatterns = [
    path('', views.panel_glowny, name='panel-glowny'),
    path('get-param-values/<str:param_code>/', views.get_param_values, name='get-param-values'),
    path('get-chart-data/', views.get_chart_data, name='get-chart-data'),
    path('get-sensor-table-data/', views.get_sensor_table_data, name='get-sensor-table-data'),
]