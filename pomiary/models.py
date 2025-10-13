from django.contrib.gis.db import models


class DGrid(models.Model):
    grid_code = models.TextField(blank=True, null=True)
    objectid = models.IntegerField(primary_key=True)
    geometry = models.GeometryField(srid=2180, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'd_grid'


class FAreaTypeDic(models.Model):
    date_from = models.CharField(max_length=10, blank=True, null=True)
    date_to = models.CharField(max_length=10, blank=True, null=True)
    area_type_cd = models.CharField(primary_key=True, max_length=10)
    area_type_name = models.CharField(max_length=255, blank=True, null=True)
    category_cd = models.CharField(max_length=15, blank=True, null=True)
    category_name = models.CharField(max_length=255, blank=True, null=True)
    area_use_cd = models.CharField(max_length=10, blank=True, null=True)
    group_category_nr = models.IntegerField(blank=True, null=True)
    grp_category_name = models.CharField(max_length=50, blank=True, null=True)
    supergr_cat_name = models.CharField(max_length=50, blank=True, null=True)
    type_fl = models.CharField(max_length=1, blank=True, null=True)
    kind_calc_area = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    kind_calc_forest = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'f_area_type_dic'


class FArodCategory(models.Model):
    pk = models.CompositePrimaryKey('arodes_int_num', 'a_year', 'prot_rank_order')
    arodes_int_num = models.IntegerField()
    prot_category_cd = models.CharField(max_length=10, blank=True, null=True)
    prot_rank_order = models.IntegerField()
    a_year = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'f_arod_category'


class FArodCue(models.Model):
    pk = models.CompositePrimaryKey('arodes_int_num', 'a_year', 'cue_rank_order')
    arodes_int_num = models.IntegerField()
    a_year = models.IntegerField()
    site_nr = models.IntegerField(blank=True, null=True)
    measure_cd = models.CharField(max_length=10, blank=True, null=True)
    urgency = models.CharField(max_length=1, blank=True, null=True)
    cutting_nr = models.IntegerField(blank=True, null=True)
    cutting_area = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    large_timber_perc = models.IntegerField(blank=True, null=True)
    cue_rank_order = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'f_arod_cue'


class FArodProtSite(models.Model):
    pk = models.CompositePrimaryKey('arodes_int_num', 'a_year', 'site_int_num')
    site_int_num = models.IntegerField()
    arodes_int_num = models.IntegerField()
    prot_site_cd = models.CharField(max_length=4, blank=True, null=True)
    prot_site_state = models.CharField(max_length=50, blank=True, null=True)
    a_year = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'f_arod_prot_site'


class FArodStorey(models.Model):
    pk = models.CompositePrimaryKey('a_year', 'arodes_int_num', 'st_rank_order_act')
    arodes_int_num = models.IntegerField()
    a_year = models.IntegerField()
    density_cd = models.CharField(max_length=5, blank=True, null=True)
    mixture_cd = models.CharField(max_length=10, blank=True, null=True)
    standdensity_index = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    tree_stock_cd = models.CharField(max_length=10, blank=True, null=True)
    st_rank_order_act = models.IntegerField()
    storey_cd = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'f_arod_storey'


class FArodes(models.Model):
    pk = models.CompositePrimaryKey('arodes_int_num', 'a_year')
    arodes_int_num = models.IntegerField()
    adress_forest = models.CharField(max_length=25, blank=True, null=True)
    a_year = models.IntegerField()
    arodes_typ_cd = models.CharField(max_length=25, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'f_arodes'


class FDegradationDic(models.Model):
    degradation_cd = models.CharField(primary_key=True, max_length=4)
    degradation_name = models.CharField(max_length=30, blank=True, null=True)
    degradation_nr = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'f_degradation_dic'


class FDensityDic(models.Model):
    date_from = models.CharField(max_length=10, blank=True, null=True)
    date_to = models.CharField(max_length=10, blank=True, null=True)
    density_cd = models.CharField(primary_key=True, max_length=5)
    density_name = models.CharField(max_length=50, blank=True, null=True)
    density_nr = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'f_density_dic'


class FEndCauseDic(models.Model):
    cause_cd = models.CharField(primary_key=True, max_length=12)
    cause_name = models.CharField(max_length=40, blank=True, null=True)
    cause_nr = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'f_end_cause_dic'


class FForestFuncDic(models.Model):
    forest_func_cd = models.CharField(primary_key=True, max_length=10)
    forest_func_name = models.CharField(max_length=50, blank=True, null=True)
    forest_func_nr = models.IntegerField(blank=True, null=True)
    date_from = models.CharField(max_length=10, blank=True, null=True)
    date_to = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'f_forest_func_dic'


class FInspectorate(models.Model):
    inspectorate_name = models.CharField(max_length=50, blank=True, null=True)
    arodes_int_num = models.IntegerField(blank=True, null=True)
    a_year = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'f_inspectorate'


class FMeasure(models.Model):
    measure_nr = models.IntegerField(blank=True, null=True)
    measure_cd = models.CharField(primary_key=True, max_length=10)
    measure_name = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'f_measure'


class FMixtureDic(models.Model):
    date_from = models.CharField(max_length=10, blank=True, null=True)
    date_to = models.CharField(max_length=10, blank=True, null=True)
    mixture_cd = models.CharField(primary_key=True, max_length=10)
    mixture_name = models.CharField(max_length=50, blank=True, null=True)
    mixture_nr = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'f_mixture_dic'


class FPartDic(models.Model):
    date_from = models.CharField(max_length=10, blank=True, null=True)
    date_to = models.CharField(max_length=10, blank=True, null=True)
    part_cd = models.CharField(primary_key=True, max_length=5)
    part_name = models.CharField(max_length=50, blank=True, null=True)
    part_nr = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'f_part_dic'


class FPlantCommDic(models.Model):
    date_from = models.CharField(max_length=10, blank=True, null=True)
    date_to = models.CharField(max_length=10, blank=True, null=True)
    plant_comm_cd = models.CharField(primary_key=True, max_length=10)
    plant_comm_name = models.CharField(max_length=255, blank=True, null=True)
    plant_comm_nr = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'f_plant_comm_dic'


class FProtCategDic(models.Model):
    date_from = models.CharField(max_length=10, blank=True, null=True)
    date_to = models.CharField(max_length=10, blank=True, null=True)
    prot_category_cd = models.CharField(primary_key=True, max_length=10)
    prot_grp_cd = models.CharField(max_length=10, blank=True, null=True)
    prot_category_name = models.CharField(max_length=50, blank=True, null=True)
    prot_category_nr = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'f_prot_categ_dic'


class FProtSiteDic(models.Model):
    prot_site_cd = models.CharField(primary_key=True, max_length=4)
    prot_site_name = models.CharField(max_length=255, blank=True, null=True)
    prot_site_prior = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'f_prot_site_dic'


class FSilvicultureDic(models.Model):
    silviculture_cd = models.CharField(primary_key=True, max_length=3)
    silviculture_name = models.CharField(max_length=50, blank=True, null=True)
    silviculture_nr = models.IntegerField(blank=True, null=True)
    date_from = models.CharField(max_length=50, blank=True, null=True)
    date_to = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'f_silviculture_dic'


class FSiteClassDic(models.Model):
    site_class_cd = models.CharField(primary_key=True, max_length=4)
    site_class_name = models.CharField(max_length=20, blank=True, null=True)
    site_class_nr = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'f_site_class_dic'


class FSiteTypeDic(models.Model):
    date_from = models.CharField(max_length=10, blank=True, null=True)
    date_to = models.CharField(max_length=10, blank=True, null=True)
    site_type_cd = models.CharField(primary_key=True, max_length=10)
    site_type_name = models.CharField(max_length=255, blank=True, null=True)
    site_type_nr = models.IntegerField(blank=True, null=True)
    site_type_grp = models.IntegerField(blank=True, null=True)
    site_type_grp_act = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'f_site_type_dic'


class FSoilSubtypeDic(models.Model):
    date_from = models.CharField(max_length=10, blank=True, null=True)
    date_to = models.CharField(max_length=10, blank=True, null=True)
    soil_subtype_cd = models.CharField(primary_key=True, max_length=10)
    soil_subtype_name = models.CharField(max_length=255, blank=True, null=True)
    soil_subtype_nr = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'f_soil_subtype_dic'


class FStandStructDic(models.Model):
    stand_struct_cd = models.CharField(primary_key=True, max_length=7)
    stand_struct_name = models.CharField(max_length=30, blank=True, null=True)
    stand_struct_nr = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'f_stand_struct_dic'


class FStoreyDic(models.Model):
    date_from = models.CharField(max_length=10, blank=True, null=True)
    date_to = models.CharField(max_length=10, blank=True, null=True)
    storey_cd = models.CharField(primary_key=True, max_length=10)
    storey_name = models.CharField(max_length=50, blank=True, null=True)
    storey_nr = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'f_storey_dic'


class FStoreySpecies(models.Model):
    pk = models.CompositePrimaryKey('arodes_int_num', 'a_year', 'storey_cd', 'sp_rank_order_act')
    arodes_int_num = models.IntegerField()
    a_year = models.IntegerField()
    storey_cd = models.CharField(max_length=10)
    sp_rank_order_act = models.IntegerField()
    species_cd = models.CharField(max_length=10, blank=True, null=True)
    species_age = models.IntegerField(blank=True, null=True)
    part_cd_act = models.CharField(max_length=3, blank=True, null=True)
    site_class_cd = models.CharField(max_length=10, blank=True, null=True)
    height = models.IntegerField(blank=True, null=True)
    bhd = models.IntegerField(blank=True, null=True)
    volume = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'f_storey_species'


class FSubarea(models.Model):
    pk = models.CompositePrimaryKey('arodes_int_num', 'a_year')
    arodes_int_num = models.IntegerField()
    a_year = models.IntegerField()
    area_type_cd = models.CharField(max_length=10, blank=True, null=True)
    site_type_cd = models.CharField(max_length=10, blank=True, null=True)
    moisture_cd = models.CharField(max_length=10, blank=True, null=True)
    degradation_cd = models.CharField(max_length=10, blank=True, null=True)
    soil_subtype_cd = models.CharField(max_length=10, blank=True, null=True)
    plant_comm_cd = models.CharField(max_length=10, blank=True, null=True)
    stand_struct_cd = models.CharField(max_length=10, blank=True, null=True)
    forest_func_cd = models.CharField(max_length=10, blank=True, null=True)
    silviculture_cd = models.CharField(max_length=10, blank=True, null=True)
    rotation_age = models.IntegerField(blank=True, null=True)
    sub_area = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    veg_cover_cd = models.CharField(max_length=10, blank=True, null=True)
    damage_degree = models.IntegerField(blank=True, null=True)
    cause_cd = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'f_subarea'


class FTreeSpeciesDic(models.Model):
    date_from = models.CharField(max_length=10, blank=True, null=True)
    date_to = models.CharField(max_length=10, blank=True, null=True)
    species_cd = models.CharField(primary_key=True, max_length=10)
    species_num = models.IntegerField(blank=True, null=True)
    species_name = models.CharField(max_length=255, blank=True, null=True)
    latin_name = models.CharField(max_length=255, blank=True, null=True)
    shrubtree_fl = models.CharField(max_length=1, blank=True, null=True)
    bot_species = models.CharField(max_length=20, blank=True, null=True)
    bot_genus = models.CharField(max_length=50, blank=True, null=True)
    bot_name = models.CharField(max_length=50, blank=True, null=True)
    fomatree_grp = models.CharField(max_length=10, blank=True, null=True)
    act_tree_grp = models.CharField(max_length=10, blank=True, null=True)
    wood_kind_fl = models.CharField(max_length=1, blank=True, null=True)
    height_grp = models.CharField(max_length=10, blank=True, null=True)
    volume_grp = models.CharField(max_length=10, blank=True, null=True)
    worth_grp = models.CharField(max_length=10, blank=True, null=True)
    c_species_cd = models.CharField(max_length=10, blank=True, null=True)
    wage_grp_fl = models.IntegerField(blank=True, null=True)
    plants_fsawing_qty = models.IntegerField(blank=True, null=True)
    plants_psawing_qty = models.IntegerField(blank=True, null=True)
    plants_foil_qty = models.IntegerField(blank=True, null=True)
    gat_grp = models.CharField(max_length=10, blank=True, null=True)
    ibl_grp = models.CharField(max_length=10, blank=True, null=True)
    lmr_reg_fl = models.CharField(max_length=10, blank=True, null=True)
    species_nr = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'f_tree_species_dic'


class GAoi(models.Model):
    gid = models.AutoField(primary_key=True)
    a_year = models.FloatField(blank=True, null=True)
    geom = models.GeometryField(srid=2180, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'g_aoi'


class GCompartments(models.Model):
    gid = models.IntegerField(blank=True, null=True)
    a_i_num = models.FloatField(blank=True, null=True)
    adr_for = models.CharField(max_length=25, blank=True, null=True)
    a_year = models.FloatField(blank=True, null=True)
    geom = models.GeometryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'g_compartments'


class GGrid(models.Model):
    grid_code = models.TextField(blank=True, null=True)
    objectid = models.TextField(blank=True, null=True)
    geometry = models.GeometryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'g_grid'


class GGrid2D(models.Model):
    gid = models.IntegerField(blank=True, null=True)
    objectid = models.FloatField(blank=True, null=True)
    grid_code = models.CharField(max_length=10, blank=True, null=True)
    srtm = models.FloatField(blank=True, null=True)
    cop = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    geom = models.GeometryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'g_grid2d'


class GGridExterior(models.Model):
    grid_code = models.TextField(blank=True, null=True)
    objectid = models.TextField(blank=True, null=True)
    geometry = models.GeometryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'g_grid_exterior'


class GSubcompartments(models.Model):
    gid = models.IntegerField(blank=True, null=True)
    a_i_num = models.FloatField(blank=True, null=True)
    adr_for = models.CharField(max_length=25, blank=True, null=True)
    area_type = models.CharField(max_length=10, blank=True, null=True)
    site_type = models.CharField(max_length=7, blank=True, null=True)
    silvicult = models.CharField(max_length=5, blank=True, null=True)
    forest_fun = models.CharField(max_length=6, blank=True, null=True)
    stand_stru = models.CharField(max_length=7, blank=True, null=True)
    rotat_age = models.IntegerField(blank=True, null=True)
    sub_area = models.FloatField(blank=True, null=True)
    prot_categ = models.CharField(max_length=9, blank=True, null=True)
    species_cd = models.CharField(max_length=9, blank=True, null=True)
    part_cd = models.CharField(max_length=3, blank=True, null=True)
    spec_age = models.IntegerField(blank=True, null=True)
    a_year = models.FloatField(blank=True, null=True)
    geom = models.GeometryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'g_subcompartments'


class GridCells(models.Model):
    grid_code = models.CharField(primary_key=True, max_length=10)

    class Meta:
        managed = False
        db_table = 'grid_cells'


class GridParamDic(models.Model):
    param_code = models.CharField(primary_key=True, max_length=50)
    param_units = models.CharField(max_length=50, blank=True, null=True)
    param_desc = models.CharField(max_length=250, blank=True, null=True)
    param_type = models.ForeignKey('GridParamTypeDic', models.DO_NOTHING, db_column='param_type')
    max_value = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    min_value = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    param_order = models.IntegerField(blank=True, null=True)
    param_info = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'grid_param_dic'


class GridParamTypeDic(models.Model):
    param_type = models.CharField(primary_key=True, max_length=10)
    type_desc = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'grid_param_type_dic'


class GridParamValues(models.Model):
    pk = models.CompositePrimaryKey('param_code', 'grid_code', 'time_stamp_id')
    grid_code = models.ForeignKey(GridCells, models.DO_NOTHING, db_column='grid_code')
    param_code = models.ForeignKey(GridParamDic, models.DO_NOTHING, db_column='param_code')
    param_value = models.CharField(max_length=50, blank=True, null=True)
    time_stamp = models.DateTimeField()
    time_stamp_id = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'grid_param_values'


class GridParamValuesCopy(models.Model):
    grid_code = models.CharField(max_length=10, blank=True, null=True)
    param_code = models.CharField(max_length=50, blank=True, null=True)
    param_value = models.CharField(max_length=50, blank=True, null=True)
    arodes_int_num = models.IntegerField(blank=True, null=True)
    time_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'grid_param_values_copy'


class GridParamValuesDic(models.Model):
    pk = models.CompositePrimaryKey('param_code', 'param_cd')
    param_code = models.ForeignKey(GridParamDic, models.DO_NOTHING, db_column='param_code')
    param_cd = models.CharField(max_length=50)
    param_description = models.CharField(max_length=250, blank=True, null=True)
    param_nr = models.IntegerField(blank=True, null=True)
    color = models.CharField(max_length=7, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'grid_param_values_dic'


class ItdAttributes(models.Model):
    gid = models.AutoField(primary_key=True)
    id = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    h = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    h_max = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    h_min = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    count = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    h_mean = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    h_median = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    h_var = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    area = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    crown_v = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    all_v = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    tt_x = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    tt_y = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    pred = models.CharField(max_length=80, blank=True, null=True)
    v = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    h_2024 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    v_2024 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    avg_ndvi23 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    avg_ndvi24 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    dead23 = models.FloatField(blank=True, null=True)
    dead24 = models.FloatField(blank=True, null=True)
    geom = models.GeometryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'itd_attributes'


class SensorData(models.Model):
    id = models.AutoField(primary_key=True)
    sensor_serial_num = models.ForeignKey('SensorSensors', models.DO_NOTHING, db_column='sensor_serial_num', blank=True, null=True)
    param = models.ForeignKey('SensorParamDic', models.DO_NOTHING, db_column='param', blank=True, null=True)
    time_stamp = models.DateTimeField(blank=True, null=True)
    data = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sensor_data'
        unique_together = (('sensor_serial_num', 'param', 'time_stamp'),)


class SensorHardware(models.Model):
    hardware_id = models.IntegerField(primary_key=True)
    model = models.CharField(max_length=50, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sensor_hardware'


class SensorParamDic(models.Model):
    parameter_cd = models.CharField(primary_key=True, max_length=10)
    parameter_description = models.CharField(max_length=100, blank=True, null=True)
    unit = models.CharField(max_length=50, blank=True, null=True)
    hobo_type = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sensor_param_dic'


class SensorSensors(models.Model):
    serial_number = models.CharField(primary_key=True, max_length=20)
    workspace_id = models.IntegerField(blank=True, null=True)
    hardware = models.ForeignKey(SensorHardware, models.DO_NOTHING, blank=True, null=True)
    latitude = models.CharField(max_length=50, blank=True, null=True)
    longitude = models.CharField(max_length=50, blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    outside = models.BooleanField(blank=True, null=True)
    logger_sn = models.CharField(max_length=20, blank=True, null=True)
    temp_factor = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sensor_sensors'


class SiatkaTest(models.Model):
    gid = models.AutoField(primary_key=True)
    id = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    left = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    top = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    right = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    bottom = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    row_index = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    col_index = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    geom = models.GeometryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'siatka_test'


class SiatkaUtm(models.Model):
    gid = models.AutoField(primary_key=True)
    objectid = models.FloatField(blank=True, null=True)
    gridname = models.CharField(max_length=254, blank=True, null=True)
    srtm = models.FloatField(blank=True, null=True)
    cop = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    number_24_majorit = models.DecimalField(db_column='24_majorit', max_digits=65535, decimal_places=65535, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    a_i_num = models.FloatField(blank=True, null=True)
    adr_for = models.CharField(max_length=26, blank=True, null=True)
    area_type_field = models.CharField(db_column='area_type_', max_length=11, blank=True, null=True)  # Field renamed because it ended with '_'.
    site_type_field = models.CharField(db_column='site_type_', max_length=9, blank=True, null=True)  # Field renamed because it ended with '_'.
    silvicult_field = models.CharField(db_column='silvicult_', max_length=5, blank=True, null=True)  # Field renamed because it ended with '_'.
    forest_fun = models.CharField(max_length=6, blank=True, null=True)
    stand_stru = models.CharField(max_length=8, blank=True, null=True)
    rotat_age_field = models.FloatField(db_column='rotat_age_', blank=True, null=True)  # Field renamed because it ended with '_'.
    sub_area_2 = models.FloatField(blank=True, null=True)
    prot_categ = models.CharField(max_length=9, blank=True, null=True)
    species_cd = models.CharField(max_length=9, blank=True, null=True)
    part_cd_23 = models.CharField(max_length=3, blank=True, null=True)
    spec_age_2 = models.FloatField(blank=True, null=True)
    a_year_23 = models.FloatField(blank=True, null=True)
    a_i_num_24 = models.FloatField(blank=True, null=True)
    adr_for_24 = models.CharField(max_length=25, blank=True, null=True)
    area_typ_2 = models.CharField(max_length=10, blank=True, null=True)
    site_typ_2 = models.CharField(max_length=7, blank=True, null=True)
    silvicul_2 = models.CharField(max_length=5, blank=True, null=True)
    forest_f_2 = models.CharField(max_length=6, blank=True, null=True)
    stand_st_2 = models.CharField(max_length=7, blank=True, null=True)
    rotat_ag_2 = models.IntegerField(blank=True, null=True)
    sub_area_1 = models.FloatField(blank=True, null=True)
    prot_cat_2 = models.CharField(max_length=9, blank=True, null=True)
    species_2 = models.CharField(db_column='species__2', max_length=9, blank=True, null=True)  # Field renamed because it contained more than one '_' in a row.
    part_cd_24 = models.CharField(max_length=3, blank=True, null=True)
    spec_age_1 = models.IntegerField(blank=True, null=True)
    a_year_24 = models.FloatField(blank=True, null=True)
    n_trees_23 = models.FloatField(blank=True, null=True)
    h_min_23 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    h_max_23 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    h_avg_23 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    n_trees_14 = models.FloatField(blank=True, null=True)
    h_min_14 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    h_max_14 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    h_mean_14 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    dtm_avg = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    geom = models.GeometryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'siatka_utm'


class SolarGeometryCalc(models.Model):
    time_stamp_id = models.BigIntegerField(primary_key=True)
    time_stamp = models.DateTimeField()
    solar_zen = models.FloatField(blank=True, null=True)
    azimuth = models.FloatField(blank=True, null=True)
    cos_t = models.FloatField(blank=True, null=True)
    ip = models.FloatField(blank=True, null=True)
    day_of_year = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'solar_geometry_calc'
