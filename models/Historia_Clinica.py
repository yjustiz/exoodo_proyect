# -*- coding: utf-8 -*-
from odoo import fields, models 

#Creando modelos (tablas de la base de datos) a partir de clases
class HistoriaClinicaPaciente(models.Model):
   _inherit= 'cad.datos.reg.turno'
   _description = 'Datos generales del paciente' 
   
   fecha_confeccion = fields.Date(string = 'Fecha Confeccion')
   
   #Edad_Debut
   edad_al_debut = fields.Selection(string = 'Edad al Debut', selection=[('dias', 'Dias'), ('meses', 'Meses'), ('años', 'Años')])
   edad_al_debut_cantidad = fields.Integer()
   
   #Tiempo_Evolucion
   tiempo_evolucion = fields.Selection(string = 'Tiempo Evolucion', selection=[('dias', 'Dias'), ('meses', 'Meses'), ('años', 'Años')])
   tiempo_evolucion_cantidad = fields.Integer(string = 'Tiempo evolucion cantidad') 
   glicemia_al_debut = fields.Float(string = 'Glicemia al Debut', digits=(16, 2))
   
   #Modo_Debut
   modo_debut = fields.Selection(string = 'Modo Debut', selection=[('síntomas_clínicos', 'Sintomas clínicos'), 
                                  ('chequeo_sin síntomas', 'Chequeo sin síntomas'), ('cetoacidosis(probada)', 'Cetoacidosis(probada)'), 
                                  ('durante_el_embarazo', 'Durante el embarazo'), ('otro', 'Otro'), ('no_sabe', 'no sabe')])
   otro_modo_debut = fields.Char(size = 30)
   
   #Obesidad_Debut
   obesidad_debut = fields.Selection(string = "Obesidad al debut", selection=[('si', 'Si'), ('no', 'No'), ('no_precisado', 'No Precisado')])    
   
   #Antecedentes_Obstetricos
   menarquia_edad = fields.Integer(string = 'Menarquia de Edad')
   embarazo = fields.Selection(string = 'Embarazo', selection=[('si', 'Si'), ('no', 'No'), ('no_precisado', 'No Precisado')])
   embarazo_cantidad = fields.Integer(string = 'Cantidad Embarazo')
   aborto_espontaneo = fields.Selection(string = 'Aborto Espontaneo', selection=[('si', 'Si'), ('no', 'No'), ('no_precisado', 'No Precisado')])
   aborto_espontaneo_cant = fields.Integer(string = 'Abortos Espontaneos Cantidad')
   malformaciones_congenitas = fields.Selection(string = 'Malformaciones congenitas', selection=[('si', 'Si'), ('no', 'No'), ('no_precisado', 'No Precisado')])
   macrofetos = fields.Selection(string = 'Macrofetos', selection=[('si', 'Si'), ('no', 'No'), ('no_precisado', 'No Precisado')])
   macrofetos_cant = fields.Integer(string = 'Cantidad Macrofetos')
   muerte_perinatal = fields.Selection(string = 'Muerte perinatal', selection=[('si', 'Si'), ('no', 'No'), ('no_precisado', 'No Precisado')])
   muerte_perinatal_cant = fields.Integer(string = 'Muerte perinatal Cantidad')
   menopausia = fields.Selection(string = 'Menopausia', selection=[('si', 'Si'), ('no', 'No'), ('no_precisado', 'No Precisado')])
   menopausia_edad = fields.Integer(string = 'Menopausia edad', size = 2 )
   fecha_ultima_mestruacion = fields.Date(string = 'Fecha Ultima Menstruacion(FUM)')
   
   #Antecedentes_Familiares_Diabetes
   via_materna = fields.Selection([('nadie', 'Nadie'), ('madre', 'Madre'), ('sobrino(a)', 'Sobrino(a)'),
                                   ('primo(a)', 'Primo(a)'), ('tio(a)', 'Tio(a)'), ('abuelo(a)', 'Abuelo(a)'),
                                   ('bisabuelo(a)', 'Bisabuelo(a)'), ('madre+abuelo(a)', 'Madre+Abuelo(a)'), ('no_sabe', 'No Sabe')])
   via_paterna = fields.Selection([('nadie', 'Nadie'), ('padre', 'Padre'), ('sobrino(a)', 'Sobrino(a)'),
                                   ('primo(a)', 'Primo(a)'), ('tio(a)', 'Tio(a)'), ('abuelo(a)', 'Abuelo(a)'),
                                   ('bisabuelo(a)', 'Bisabuelo(a)'), ('padre+abuelo(a)', 'Padre+Abuelo(a)'), ('no_sabe', 'No Sabe')])
   hermano = fields.Selection(string = 'Hermano', selection=[('si', 'Si'), ('no', 'No'), ('no_sabe', 'No sabe')])
   hijo = fields.Selection(string = 'Hijo', selection=[('si', 'Si'), ('no', 'No'), ('no_sabe', 'No sabe')])
   comentario = fields.Char(size = 150)
   
   #Antecedente_Patologicos_Personales
   hiperlipoproteinemia_p = fields.Selection(string = 'Hiperlipoproteinemia', selection=[('si', 'Si'), ('no', 'No'), ('no_precisado', 'No Precisado')])
   hipertension_arterial_p = fields.Selection(string = 'Hipertensión Arterial', selection=[('si', 'Si'), ('no', 'No'), ('no_precisado', 'No Precisado')])
   cardiopatia_isquemica_p = fields.Selection(string = 'Cardiopatía Isquemica', selection=[('si', 'Si'), ('no', 'No'), ('no_precisado', 'No Precisado')])
   claudicacion_intermitente_p = fields.Selection(string = 'Claudicación Intermitente',selection=[('si', 'Si'), ('no', 'No'), ('no_precisado', 'No Precisado')])
   otros = fields.Selection(string='Otros', selection=[('si', 'Si'), ('no', 'No'), ('no_precisado', 'No Precisado')])
   otros_especificar = fields.Char(string='Otros(especificar)', size = 150)
   
   #Antecedente_Patologicos_Familiares
   hiperlipoproteinemia_f = fields.Selection(string='Hiperlipoproteinemia', selection=[('si', 'Si'), ('no', 'No'), ('no_precisado', 'No Precisado')])
   hipertension_arterial_f = fields.Selection(string='Hipertensión Arterial', selection=[('si', 'Si'), ('no', 'No'), ('no_precisado', 'No Precisado')])
   cardiopatia_isquemica_f = fields.Selection(string='Cardiopatía Isquemica', selection=[('si', 'Si'), ('no', 'No'), ('no_precisado', 'No Precisado')])
   
   #Habitos_Toxicos    
   habitos_toxico = fields.Selection(string = 'Hábitos Tóxico', selection=[('no_fumador', 'No Fumador'), 
                               ('ex_fumador(6_meses_sin_fumar)', 'Ex Fumador(6 meses sin fumar)'), 
                               ('fumador', 'Fumador')])
   annos_fumador = fields.Integer(string = 'HT_Años Fumador')
   annos_ex_fumador = fields.Integer(string = 'HT_Años Ex Fumador')
   tabaquismo = fields.Selection(string = 'Tabaquismo', selection=[('cigarros', 'Cigarros'), ('tabacos', 'Tabacos')])
   tabaquismo_cantidad = fields.Integer(string = 'Tabaquismo Cantidad/dia')
   alcohol = fields.Selection(string = 'Alcohol', selection=[('no', 'No'), ('si', 'Si')])
   alcohol_gramos = fields.Selection(string = 'Alcohol gramos/dia', selection=[('ocasional', 'Ocasional'), 
                               ('semanal', 'Semanal'), ('diario', 'Diario'), ('mensual', 'Mensual'), 
                               ('frecuente', 'Frecuente')])
   #Tratamiento_Inicio
   tratamiento_inicio = fields.Selection(string = 'Tratamiento Al Inicio', selection=[('sólo_dieta', 'Sólo dieta'), ('coh', 'COH'), ('insulina', 'Insulina'), ('insulina+coh', 'Insulina+COH'), ('no_precisado', 'No precisado'), ('no_tenía', 'No tenía')])
   #tratamiento_inic_medicament = fields.Char(string = 'Tratamiento Inicio Medicamentos', size = 250)
   anno_comienzo = fields.Date(string = 'Año de comienzo')       
   
   #Tratamiento_Actual
   tratamiento_actual = fields.Selection(string = 'Tratamiento Actual', selection=[('sólo_dieta', 'Sólo dieta'), ('coh', 'COH'), ('insulina', 'Insulina'), ('insulina+coh', 'Insulina+COH'), ('no_precisado', 'No precisado')])
   #tratamiento_fin_medicament = fields.Char(string = 'Tratamiento Final Medicamentos', size = 250)
   anno_comienzo_f = fields.Date(string = 'Año de comienzo')
   
   #Sintomas_actuales
   sintoma_actuales = fields.Text(string = 'Síntomas actuales')
   
   #Examen_Fisico
   examen_fisico = fields.Html(string = 'Examen Físico')
   
   #Estudio_Socio_Laboral
   estudio_socio_laboral = fields.Char(string = 'Estudio Socio Laboral', size = 25)
   
   #Medida_Paciente    
   talla = fields.Float(string='Talla del Paciente', digits=(3, 2), default = 0.0)
   peso = fields.Float(string = 'Peso', digits=(3, 2), default = 0.0)
   indice_masa_corp = fields.Float(string='Indice Masa Corporal', digits=(3,2), default = 0.0)
   evaluacion_nutricional = fields.Selection(string = 'Evaluación Nutricional', selection=[('bajo_peso', 'Bajo Peso'), ('normo_peso', 'Normo Peso'), 
                           ('sobre_peso_grado_I', 'Sobre Peso Grado I'), ('sobre_peso_grado_II', 'Sobre Peso Grado II'), ('obesidad_grado_I', 'Obesidad grado I'), 
                           ('obesidad_grado_II', 'Obesidad Grado II'), ('obesidad_grado_III', 'Obesidad Grado III')]) 
   ta_acostado_sistolica = fields.Float(string = 'TA acostado Sistólica', digits=(3,2), default=0.0)
   ta_acostado_diastolica = fields.Float(string = 'TA acostado Diastólica', digits=(3,2), default=0.0)
   ta_parado_sistolica = fields.Float(string = 'TA Parado Sistólica', digits=(3,2), default=0.0)
   ta_parado_diastolica = fields.Float(string = 'TA Parado Diastólica', digits=(3,2), default=0.0)
   frecuencia_cardiaca = fields.Integer(string = 'Frecuencia cardiaca')
   circunferencia_abdominal = fields.Integer(string = 'Circunferencia Abdominal')
   circunferencia_cadera = fields.Integer(string = 'Circunferencia Cadera')     
   
   #Conocimiento_Previo_Ingreso
   dieta = fields.Selection(string = 'Dieta', selection=[('si', 'Si'), ('no', 'No')])
   automonitoreo = fields.Selection(string = 'Automonitoreo', selection=[('si', 'Si'), ('no', 'No')])
   cuidado_pies = fields.Selection(string = 'Cuidado_Pies', selection=[('si', 'Si'), ('no', 'No')])
   hipoglicemia = fields.Selection(string = 'Hipoglicemia', selection=[('si', 'Si'), ('no', 'No')])
   complicacione = fields.Selection(string = 'Complicaciones', selection=[('si', 'Si'), ('no', 'No')])
   autoajuste_tratamiento = fields.Selection(string = 'Autoajuste Tratamiento', selection=[('si', 'Si'), ('no', 'No')])
   
   #Resultado_Educacion_Diabetologica    
   resultado_inicial = fields.Selection(string = 'Resultado Inicial', selection=[('deficiente', 'Deficiente'), ('mínimo_suficiente', 'Mínimo Suficiente'), ('satisfactorio', 'Satisfactorio'), ('excelente', 'Excelente')])
   resultado_final = fields.Selection(string = 'Resultado Final', selection=[('deficiente', 'Deficiente'), ('mínimo_suficiente', 'Mínimo Suficiente'), ('satisfactorio', 'Satisfactorio'), ('excelente', 'Excelente')])
   
   #Examen_Miembros_Inferiores   
   amputacione_der = fields.Selection(string = 'Amputaciones Derechas', selection=[('no', 'No'), ('dedos', 'Dedos'), ('abajo_del_tobillo', 'Abajo del Tobillo'), ('arriba_del_tobillo', 'Arriba del Tobillo'), ('arriba_de_la_rodilla', 'Arriba de la Rodilla'), 
                                    ('no_precisado', 'No Precisado')])
   amputacione_izq = fields.Selection(string = 'Amputaciones Izquierda', selection=[('no', 'No'), ('dedos', 'Dedos'), ('abajo_del_tobillo', 'Abajo del Tobillo'), ('arriba_del_tobillo', 'Arriba del Tobillo'), ('arriba_de_la_rodilla', 'Arriba de la Rodilla'), 
                                    ('no_precisado', 'No Precisado')])
   apariencia_isquemica_der = fields.Selection(string = 'Apariencia Isquemica Derecha', selection=[('presente', 'Presente'), ('ausente', 'Ausente'), ('no_precisado', 'No Precisado')])
   apariencia_isquemica_izq = fields.Selection(string = 'Apariencia Isquemica Izquierda', selection=[('presente', 'Presente'), ('ausente', 'Ausente'), ('no_precisado', 'No Precisado')]) 
   pulso_pedio_der = fields.Selection(string = 'Pulso Pedio Derecho', selection=[('presente', 'Presente'), ('disminuido', 'Disminuido'), ('ausente', 'Ausente'), ('no_precisado', 'No Precisado')])
   pulso_pedio_izq = fields.Selection(string = 'Pulso Pedio Izquierdo', selection=[('presente', 'Presente'), ('disminuido', 'Disminuido'), ('ausente', 'Ausente'), ('no_precisado', 'No Precisado')])
   pulso_tibial_posterior_der = fields.Selection(string = 'Pulso Tibial Derecha', selection=[('presente', 'Presente'), ('disminuido', 'Disminuido'), ('ausente', 'Ausente'), ('no_precisado', 'No Precisado')])
   pulso_tibial_posterior_izq = fields.Selection(string = 'Pulso Tibial Izquierda', selection=[('presente', 'Presente'), ('disminuido', 'Disminuido'), ('ausente', 'Ausente'), ('no_precisado', 'No Precisado')])
   lesiones_ulcerosas_der = fields.Selection(string = 'Lesiones Ulcerosas Derechas', selection=[('no', 'No'), ('vascular', 'Vascular'), ('neuropática', 'Neuropática'), ('mixtas', 'Mixtas'), ('no_precisado', 'No precisado')])
   lesiones_ulcerosas_izq = fields.Selection(string = 'Lesiones Ulcerosas Izquierda', selection=[('no', 'No'), ('vascular', 'Vascular'), ('neuropática', 'Neuropática'), ('mixtas', 'Mixtas'), ('no_precisado', 'No precisado')])
   reflejo_rotuliano_der = fields.Selection(string = 'Reflejo Rotuliano Derecha', selection=[('presente', 'Presente'), ('hiporreflexia', 'Hiporreflexia'), ('arreflexia', 'Arreflexia'), ('no_precisado', 'No precisado')])
   reflejo_rotuliano_izq = fields.Selection(string = 'Reflejo Rotuliano Izquierda', selection=[('presente', 'Presente'), ('hiporreflexia', 'Hiporreflexia'), ('arreflexia', 'Arreflexia'), ('no_precisado', 'No precisado')])
   palestesia_der = fields.Selection(string = 'Palestesia Derecha', selection=[('normal', 'Normal'), ('hipopalestesia', 'Hipopalestesia'), ('apalestesia', 'Apalestesia'), ('no_precisado', 'No precisado')])
   palestesia_izq = fields.Selection(string = 'Palestesia Izquierda', selection=[('normal', 'Normal'), ('hipopalestesia', 'Hipopalestesia'), ('apalestesia', 'Apalestesia'), ('no_precisado', 'No precisado')])
   
   #Complementarios
   glucemia_ay = fields.Float(string = 'Glucemia_ay')
   glucemia_pp_2h = fields.Float(string = 'Glucemia_pp2h')
   hba_1c = fields.Float(string = 'Hba1c')
   colesterol = fields.Float(string = 'Colesterol')
   trigliceridos = fields.Float(string = 'Trigliceridos')
   hdl_col = fields.Float(string = 'HDL-Col')
   creatinina = fields.Float(string = 'Creatinina')
   microalbuminuria = fields.Float(string = 'Microalbuminuria')
   filtrado_glomerular_sangre = fields.Float(string = 'Filtrado Glomerular Sangre')
   filtrado_glomerular_ckd_epi = fields.Float(string = 'Filtrado Glomerular CKD EPI')
   filtrado_glomerular_orina = fields.Float(string = 'Filtrado Glomerular Orina 24h')
   hc_hemoglobina = fields.Float(string = 'HC Hemoglobina')
   hc_Leucocito = fields.Float(string = 'HC Leucocito')
   hc_hematrocito = fields.Float(string = 'HC Hematrocito')
   hc_eritrosedimentacion = fields.Float(string = 'HC Eritrosedimentacion')
   conteo_addis_proteina = fields.Char(string = 'Conteo Addis Proteína')
   conteo_addis_leucocito = fields.Integer(string = 'Conteo Addis Leucocito')
   conteo_addis_hematios = fields.Integer(string = 'Conteo Addis Hematios')
   conteo_addis_cilindro = fields.Integer(string = 'Conteo addis Cilindro') 
   tgp = fields.Float(string = 'TGP')
   tgo = fields.Float(string = 'TGO')
   ggt = fields.Float(string = 'GGT')
   falc = fields.Float(string = 'FALC')
   urato = fields.Float(string = 'Urato') 
   proteina_c_reactiva = fields.Float(string = 'Proteína C Reactiva')
   cistatina_c = fields.Float(string = 'Cistatina C')
   complem_otros = fields.Char(string = 'Otros', size=30)
   
   #Complicaciones
   vision_borrosa = fields.Selection(string = 'Visión Borrosa', selection=[('si', 'Si'), ('no', 'No')])
   vision_ojo_derecho = fields.Selection(string = 'Vision Ojo Derecho', selection=[('normal', 'Normal'), ('minusvalido', 'Minusválido'), ('moderado', 'Moderado'), ('ciego', 'Ciego'), ('no_precisado', 'No Precisado')])
   vision_ojo_izquierdo = fields.Selection(string = 'Visión Ojo Izquierdo', selection=[('normal', 'Normal'), ('minusvalido', 'Minusválido'), ('moderado', 'Moderado'), ('ciego', 'Ciego'), ('no_precisado', 'No Precisado')])
   retinopatia_diabetica = fields.Selection(string = 'Retinopatía Diabética', selection=[('no', 'No'), ('no_proliferativa', 'No Proliferativa'), ('proliferativa', 'Proliferativa'), ('no_precisado', 'No Precisado')]) 
   retinopatia_hipertensiva = fields.Selection(string = 'Retinopatía Hipertensiva', selection=[('no', 'No'), ('grado_1', 'Grado 1'), ('grado_2', 'Grado 2'), ('grado_3', 'Grado 3'), ('grado_4', 'Grado 4'), ('no_precisado', 'No Precisado')])
   retinopatia_arteroesc = fields.Selection(string = 'Retinopatía Arteroesc.', selection=[('no', 'No'), ('grado_1', 'Grado 1'), ('grado_2', 'Grado 2'), ('grado_3', 'Grado 3'), ('grado_4', 'Grado 4'), ('no_precisado', 'No Precisado')]) 
   hemorragia_vitrea_od = fields.Selection(string = 'Hemorragia Vitrea OD', selection=[('no', 'No'), ('si', 'Si'),('no_precisado', 'No Precisado')])
   hemorragia_vitrea_oi = fields.Selection(string = 'Hemorragia Vitrea OI', selection=[('no', 'No'), ('si', 'Si'),('no_precisado', 'No Precisado')])
   maculopatia_od = fields.Selection(string = 'Maculopatía OD', selection=[('no', 'No'), ('si', 'Si'), ('no_precisado', 'No Precisado')])
   maculopatia_oi = fields.Selection(string = 'Maculopatia OI', selection=[('no', 'No'), ('si', 'Si'), ('no_precisado', 'No Precisado')])
   catarata = fields.Selection(string = 'Catarata', selection=[('no', 'No'), ('metabolica', 'Metabólica'), ('senil', 'Senil'), ('otras', 'Otras'), ('no_precisado', 'No Precisado')])
   glaucoma = fields.Selection(string = 'Glaucoma', selection=[('no', 'No'), ('ang_abierto', 'Ang. Abierto'), ('secundario', 'Secundario'), ('ang_estrecho', 'Ang. Estrecho'), ('no_precisado', 'No Precisado')])
   nefropatia = fields.Selection(string = 'Nefropatía', selection=[('si', 'Si'), ('no', 'No'), ('no_precisado', 'No Precisado')])
   accidente_vascular_cerebral = fields.Selection(string = 'Accidente Vascular Cerebral', selection=[('si', 'Si'), ('no', 'No'), ('no_precisado', 'No Precisado')])
   cardiopatia_isquemica = fields.Selection(string = 'Cardiopatía Isquemica', selection=[('si', 'Si'), ('no', 'No'), ('no_precisado', 'No Precisado')])
   pie_isquemico = fields.Selection(string = 'Pie_ Isquemico', selection=[('si', 'Si'), ('no', 'No'), ('no_precisado', 'No Precisado')])
   mal_perforante = fields.Selection(string = 'Mal Perforante', selection=[('si', 'Si'), ('no', 'No'), ('no_precisado', 'No Precisado')]) 
   polineuropatia_periferica = fields.Selection(string = 'Polineuropatía Periférica', selection=[('si', 'Si'), ('no', 'No'), ('no_precisado', 'No Precisado')])
   mononeuropatia = fields.Selection(string = 'Mononeuropatía', selection=[('si', 'Si'), ('no', 'No'), ('no_precisado', 'No Precisado')])
   dse = fields.Selection(string = 'DSE', selection=[('si', 'Si'), ('no', 'No'), ('no_precisado', 'No Precisado')])
   vejiga_neurogenica = fields.Selection(string = 'Vejiga Neurogénica', selection=[('si', 'Si'), ('no', 'No'), ('no_precisado', 'No Precisado')])
   sepsis = fields.Selection(string = 'Sepsis', selection=[('si', 'Si'), ('no', 'No'), ('no_precisado', 'No Precisado')])
   dermopatia = fields.Selection(string = 'Dermopatía', selection=[('si', 'Si'), ('no', 'No'), ('no_precisado', 'No Precisado')])
   hiperlipoproteinemia_c = fields.Selection(string = 'Hiperlipoproteinemia', selection=[('si', 'Si'), ('no', 'No'), ('no_precisado', 'No Precisado')])
   neuropatia_autonomica = fields.Selection(string = 'Neuropatia Autonomica', selection=[('si', 'Si'), ('no', 'No'), ('no_precisado', 'No Precisado')]) 
   otras_complicaciones = fields.Selection(string = 'Otras Complicaciones', selection=[('si', 'Si'), ('no', 'No'), ('no_precisado', 'No Precisado')])
   hipertension_arterial_c = fields.Selection(string = 'Hipertension Arterial', selection=[('si', 'Si'), ('no', 'No'), ('no_precisado', 'No Precisado')]) 
   
   #Diagnostico_Definitivo
   diagnostico_definitivo = fields.Selection(string = 'Diagnóstico Definitivo(Tipo de DM)', selection=[('diabetes_mellitus_tipo_I', 'Diabetes Mellitus Tipo I'), ('diabetes_mellitus_tipo_II', 'Diabetes Mellitus Tipo II'),                                        ('diabetes_mellitus_tipo_lada', 'Diabetes Mellitus Tipo LADA'), ('diabetes_mellitus_pre-gestacional', 'Diabetes Mellitus Pre-Gestacional'),
                                    ('diabetes_mellitus_gestacional', 'Diabetes Mellitus Gestacional'), ('diabetes_mellitus_inducido_x_medicamentos', 'Diabetes Mellitus Inducido x Medicamentos'), ('diabetes_mellitus_por_glucocorticoides(dexametaso)', 'Diabetes Mellitus por glucocorticoides (Dexametaso)')])
   
   #Otras Enfermedades
   otras_enfermedades = fields.Text(string = 'Otras Enfermedades')
   
   #Indicaciones_Tratamiento
   dieta_calorias = fields.Integer(string = 'Dieta en Calorías')
   ejercicios = fields.Text(string = 'Ejercicios')
   tratamiento_normoglucemiante = fields.Text(string = 'Tratamiento normoglucemiante')
   otros_tratamiento_indicaciones = fields.Text(string = 'Otros Tratamientos e indicaciones')
   evolucion_en_ingreso = fields.Text(string = 'Evolución en el Ingreso')
   seguimiento = fields.Text(string = 'Seguimiento')
   evoluciones = fields.Html(string = 'Evoluciones')        
   
   #-----------------------------------------------------------------------#
   #                 METODOS PARA HISTORIAS CLINICAS                       #
   #-----------------------------------------------------------------------#
   
   #usar esta funcion de ejemplo para validar valores
    #_sql_constraints = [
    #    (
    #        'check_amount_not_negative',
    #        'CHECK(amount >= 0.0)',
    #        "The payment amount cannot be negative.",
    #    ),
    #]