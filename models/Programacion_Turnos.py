# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError
from datetime import date, datetime

#Creando modelos (tablas de la base de datos) a partir de clases

class Turno(models.Model):
    _name = 'cad.prog.turno'
    _rec_name = "no_folio"

    
    @api.depends('fecha_inicio')
    def compute_anno(self):
        """Devuelve el año de la fecha especificada en el
            campo 'fecha_inicio' """
        for record in self:
            if record.fecha_inicio:
                record.anno = record.fecha_inicio.year
            else:
                record.anno = '' 
    
#Datos para reservar turno
    no_folio = fields.Integer(string = 'FOLIO NO.', required = True)
    
    fecha_inicio = fields.Date(required = True)
    fecha_fin = fields.Date(required = True)#calculado de fecha dado 5 dias 
    anno = fields.Char(string = 'Año', compute = compute_anno, store = True)
    
    dia_de_semana = fields.Selection(string='Día del Turno', selection=[('lunes', 'Lunes'), ('martes', 'Martes'), ('miércoles', 'Miércoles'), ('jueves', 'Jueves'), ('viernes', 'Viernes')], default='lunes') 
    mes_del_turno = fields.Selection(string='Mes del Turno', selection=[('1', 'Enero'), ('2', 'Febrero'),('3', 'Marzo'), ('4', 'Abril'), ('5', 'Mayo'), ('6', 'Junio'),('7', 'Julio'), ('8', 'Agosto'), ('9', 'Septiembre'),('10', 'Octubre'), ('11', 'Noviembre'), ('12', 'Diciembre')])
    
    datos_reg_ids = fields.One2many('cad.datos.reg.turno','turno_id',string='Listado de Pacientes')
    state = fields.Selection(string='Estado',selection=[('draft', 'Borrador'),
                        ('open','En curso'),('confirm', 'Confirmado')],default="draft")
    max_elemento = fields.Integer(string='Capacidad del Centro', default=24)
        
#-----------------------------------------------------------------------#
#                            METODOS                                    #
#-----------------------------------------------------------------------#
    #validar los numero de HC del curso
    
    def addmovhsp(self):
        """Pasa para el otro estado los pacientes registrados en el turno"""
        if self.state=='draft' and (self.datos_reg_ids!=False and len(self.datos_reg_ids.ids)!=0):
           self.write({'state': "open"})
           for i in self.datos_reg_ids:
               i.write({'state': "open"})
        else:
            raise ValidationError(_('No hay pacientes registrados'))
    
    #Cierra el curso
    def cerrar_curso(self):
        """Metódo para terminar el curso y confirma el estado del
            registro que sea confirmado o cancelado, sino no puede 
            terminar el curso
            """
        self.write({'state': "confirm"})
         #q validar para poder confirmar
         #esto es cabrona
        for i in self.datos_reg_ids:
            if i.state_hist_clinic == 'confirme':
                raise ValidationError(_('Hay registro para confirmar o cancelar.Por favor verifique los registros!'))
            else:
                i.write({'state': "confirm"})
    
    #Este registro se oculto el boton hasta definir donde utilizarlo si se necesita
    #Metódo para enviar los registros en {state : 'open'} a {state : 'draft'}
    def envborrad(self):
        if self.state == 'open':
            self.write({'state': "draft"})
        else:
            raise ValidationError(_('Hay registro confirmado !'))
            
    def info_box(self):
        pass
    
class DatosRegistroTurno(models.Model):
    _name= 'cad.datos.reg.turno'
    
    
    #Creando secuencia para el turno
    @api.model
    def create(self, vals):
        if vals.get('numero_turno', _('New')) == _('New'):
            vals['numero_turno']= self.env['ir.sequence'].next_by_code('cad.datos.reg.turno') or _('New')
        result = super(DatosRegistroTurno, self).create(vals)
        return result
    
    #datos generales 
    numero_turno = fields.Char(string='No. Turno', required = True, copy = False, readonly = True,
                                index = True, default = lambda self: _('New'))
     
    def numturno(self):
         pass
    
    ''' @api.One
    @api.depends('primer_apellido','segundo_apellido')
    def _get_last(self):
        self.nombre_apellidos_id = 'Nombre del Paciente' + self.primer_apellido + self.segundo_apellido  '''
         
    turno_id = fields.Many2one('cad.prog.turno',string='Turno',required=False)
    #Estados
    state = fields.Selection([('draft', 'Borrador'),('open','En curso'),('delete', 'Cancelado'),('confirm', 'Confirmado')],default="draft")
    state_hist_clinic = fields.Selection(string = 'Estado Historia Clínica', selection=[('confir', 'Confirmado'), ('cancel','Cancelado'), ('confirme','Confirme')],default="confirme")
    
    # datos del paciente
    nombre_apellidos_id = fields.Many2one(comodel_name = 'cad.paciente',string = 'Nombre del Paciente')
     
     #hoja de ingreso
    remitido = fields.Selection(string = 'Remitido', selection=[('area_salud','Area Salud'), ('endocrino','Endocrino'), ('otros_centros','Otros Centros')], help = 'Por quien fue remitido')
    area_salud = fields.Selection(string = 'Area de salud', selection=[('julian_grimau', 'Julian Grimau'), ('carlos_j_finlay', 'Carlos J. Finlay'), ('distrito_josé_martí', 'Distrito José Martí'), 
                        ('frank_país', 'Frank País'), ('camilo_torres', 'Camilo Torres'), ('lopez_peña', 'Lopez Peña'), ('28_de_septiembre', '28 de Septiembre'), ('municipal', 'Municipal'), ('armando_garcia', 'Armando García'), ('30_de_noviembre', '30 de Noviembre'), ('josue_país', 'Josue País'), ('poblados', 'Poblados'), ('otros_municipios', 'Otros Municipios'), ('otras_provincias', 'Otras Provincias')])
    consultorio_medico = fields.Integer(string = 'Consultorio Médico', help ='Número del consultorio') 
    escolaridad = fields.Selection(string = 'Escolaridad', selection=[('primaria', 'Primaria'), ('primaria_no_terminada', 'Primaria no Terminada'), ('secundaria', 'Secundaria'), ('pre-universitario', 'Pre-Universitario'), ('universitario', 'Universitario')])
    ocupacion = fields.Selection(string = 'Ocupacion', selection=[('ama_de_casa', 'Ama de Casa'), ('trabajador', 'Trabajador'),('jubilado', 'Jubilado'), ('estudiante', 'Estudiante'), ('s/ocupación', 'S/Ocupación'), ('cuentapropista', 'Cuentapropista')])
     
    carnet_identidad = fields.Char(related='nombre_apellidos_id.carnet_identidad')
    historia_clinica = fields.Char(related='nombre_apellidos_id.historia_clinica')
    primer_apellido = fields.Char(related='nombre_apellidos_id.primer_apellido')
    segundo_apellido = fields.Char(related='nombre_apellidos_id.segundo_apellido')
    sexo = fields.Selection(related='nombre_apellidos_id.sexo')
    color_piel = fields.Selection(related='nombre_apellidos_id.color_piel')
    edad_actual = fields.Integer(related='nombre_apellidos_id.edad_actual')
    #Datos de la dirección
    calle = fields.Char(related='nombre_apellidos_id.calle')
    numero = fields.Char(related='nombre_apellidos_id.numero')
    entre_calles = fields.Char(related='nombre_apellidos_id.entre_calles')
    ciudad_o_pueblo = fields.Char(related='nombre_apellidos_id.ciudad_o_pueblo')
    #Datos de Provincia o Municipio
    provincia = fields.Selection(related='nombre_apellidos_id.provincia')
    municipio_id = fields.Selection(related='nombre_apellidos_id.municipio_id')
    #Datos de la profesión
    profesion = fields.Char(related='nombre_apellidos_id.profesion')
    #Datos de teléfono de contactos
    phone_movil = fields.Char(related='nombre_apellidos_id.phone_movil')
    telefono_trabajo = fields.Char(related='nombre_apellidos_id.telefono_trabajo')
    telefono_casa = fields.Char(related='nombre_apellidos_id.telefono_casa')
    #Datos del Acompañante
    nombre_apellidos_acomp = fields.Char(related='nombre_apellidos_id.nombre_apellidos_acomp')
    direccion_acomp = fields.Char(related='nombre_apellidos_id.direccion_acomp')
    telefono_acomp = fields.Char(related='nombre_apellidos_id.telefono_acomp')
    activo = fields.Boolean(related='nombre_apellidos_id.activo')
    
    #@api.multi
    def confir_historia_clinic(self):
        """Verifica que los campos de la HC no esten vacíos, sino no permite confirmar el registro"""
        if self.edad_al_debut_cantidad != False:
            self.write({'state_hist_clinic':'confir'})
        else:
            raise ValidationError('No se puede confirmar hay campos vacíos en la Historia Clínica')
    
    def cancel_historia_clinic(self):
        self.write({'state_hist_clinic':'cancel'})
        
        
    #buscar para que puede servir
    #MONTH_SELECTION = [
    #   ('1', 'January'),
    #   ('2', 'February'),
    #   ('3', 'March'),
    #   ('4', 'April'),
    #   ('5', 'May'),
    #   ('6', 'June'),
    #   ('7', 'July'),
    #   ('8', 'August'),
    #   ('9', 'September'),
    #   ('10', 'October'),
    #   ('11', 'November'),
    #   ('12', 'December'),