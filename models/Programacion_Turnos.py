# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError

#Creando modelos (tablas de la base de datos) a partir de clases

class Turno(models.Model):
    _name= 'cad.prog.turno'
    _rec_name="no_folio"
#Datos para reservar turno
    no_folio  = fields.Integer("FOLIO NO.", required=True)
    anno = fields.Char("Año")
    fecha_inicio  = fields.Date(required= True)
    fecha_fin = fields.Date(required=True)#calculado de fecha dado 5 dias 

    dia_de_semana = fields.Selection(string='Día del Turno', selection=[('lunes', 'Lunes'),('martes', 'Martes'), ('miércoles', 'Miércoles'), ('jueves', 'Jueves'), ('viernes', 'Viernes')], default='lunes') 
    mes_del_turno = fields.Selection(string='Mes del Turno', selection=[('enero', 'Enero'), ('febrero', 'Febrero'),('marzo', 'Marzo'), ('abril', 'Abril'), ('mayo', 'Mayo'), ('junio', 'Junio'),('julio', 'Julio'), ('agosto', 'Agosto'), ('septiembre', 'Septiembre'),('octubre', 'Octubre'), ('noviembre', 'Noviembre'), ('diciembre', 'Diciembre')])
    hora_del_turno = fields.Selection(string='Hora del Turno', selection=[('7:00 am', '7:00 AM'), ('8:00 am', '8:00 AM')]) #Quitar este campo de base de datos
    
    datos_reg_ids = fields.One2many('cad.datos.reg.turno','turno_id',string='Listado de Pacientes')
    state = fields.Selection(string='Estado',selection=[('draft', 'Borrador'),('open','En curso'),('confirm', 'Confirmado')],default="draft")
    max_elemento = fields.Integer(string='Capacidad del Centro', default=24)
    #state_hist_clinic = fields.Selection(string = 'Estado Historia Clínica', selection=[('confir', 'Confirmado'), ('cancel','Cancelado'), ('confirme','Confirme')],default='confirme')
    #fin de datos del turno
    
    
   #-----------------------------------------------------------------------#
   #                            METODOS                                    #
   #-----------------------------------------------------------------------#
    def addmovhsp(self):
       #validar los numero de HC del curso
       #movi_hosp_curso=self.env['cad.movi_hosp_curso']
       #movi_hosp_curso.create({'turno_id':self.id,'fecha_registrado':self.fecha_inicio,'datos_pacientes_ids':[(0,0,{'datos_reg_id':self.datos_reg_ids[0].id}),(0,0,{'datos_reg_id':self.datos_reg_ids[1].id})]})
       #pass
       if self.state=='draft' and (self.datos_reg_ids!=False and len(self.datos_reg_ids.ids)!=0):
           self.write({'state': "open"})
           for i in self.datos_reg_ids:
               i.write({'state': "open"})
       else:
            raise ValidationError(_('No hay pacientes registrados'))
    
    def cerrar_curso(self):
         self.write({'state': "confirm"})
         #q validar para poder confirmar
         #esto es cabrona
         for i in self.datos_reg_ids:
             i.write({'state': "confirm"})
    
    def confirmar_registro(self):
        pass
        #self.move_id.button_cancel()
    
    def action_confir(self):
        pass
        #''' open -> confirmado '''
        #self.move_id.button_cancel()
        
    def action_cancel(self):
        pass
        #''' draf -> cancelled '''
        #self.move_id.button_cancel()    
    
    def info_box(self):
        pass
        
    
class DatosRegistroTurno(models.Model):
    _name= 'cad.datos.reg.turno'
    #datos generales 
    numero_turno = fields.Char(string='No. Turno', required = True, copy = False, readonly = True,
                                index = True, default = lambda self: _('New'))
     
    def numturno(self):
         pass
     
      #Creando secuencia para el turno
    @api.model
    def create(self, vals):
        if vals.get('numero_turno', _('New')) == _('New'):
            vals['numero_turno']= self.env['ir.sequence'].next_by_code('cad.datos.reg.turno') or _('New')
        result = super(DatosRegistroTurno, self).create(vals)
        return result
         
    turno_id = fields.Many2one('cad.prog.turno',string='Turno',required=False)
    state = fields.Selection([('draft', 'Borrador'),('open','En curso'),('delete', 'Cancelado'),('confirm', 'Confirmado')],default="draft")
    state_hist_clinic = fields.Selection(string = 'Estado Historia Clínica', selection=[('confir', 'Confirmado'), ('cancel','Cancelado'), ('confirme','Confirme')],default="confirme")
    # datos del paciente
    nombre_apellidos_id = fields.Many2one('cad.paciente',string='Nombre del Paciente', required=True)
     #nombre_apellidos = fields.Many2one('cad.paciente',string='Nombre del Paciente')
     
     #hoja de ingreso
    remitido = fields.Selection(string='Remitido', selection=[('area salud','Area Salud'), ('endocrino','Endocrino'), ('otros centros','Otros Centros')], help = 'Por quien fue remitido')
    area_salud = fields.Selection([('julian grimau', 'Julian Grimau'), ('carlos j. finlay', 'Carlos J. Finlay'), ('distrito josé martí', 'Distrito José Martí'), 
                        ('frank país', 'Frank País'), ('camilo torres', 'Camilo Torres'), ('lopez peña', 'Lopez Peña'), ('28 de septiembre', '28 de Septiembre'),
                        ('municipal', 'Municipal'), ('armando garcia', 'Armando García'), ('30 de noviembre', '30 de Noviembre'), ('josue país', 'Josue País'), 
                        ('poblados', 'Poblados'), ('otros municipios', 'Otros Municipios'), ('otras provincias', 'Otras Provincias')])
    consultorio_medico = fields.Integer(string = 'Consultorio Médico', help ='Número del consultorio')
    escolaridad = fields.Selection(string = 'Escolaridad', selection=[('primaria', 'Primaria'), ('primaria no terminada', 'Primaria no Terminada'),
                        ('secundaria', 'Secundaria'), ('12mo. grado', '12mo. Grado'), ('pre-universitario', 'Pre-Universitario'), 
                        ('universitario', 'Universitario')])
    ocupacion = fields.Selection(string='Ocupacion', selection=[('ama de casa', 'Ama de Casa'), ('trabajador', 'Trabajador'),('jubilado', 'Jubilado'), ('estudiante', 'Estudiante'), ('s/ocupación', 'S/Ocupación'), ('cuentapropista', 'Cuentapropista')])
     
    carnet_identidad = fields.Char(related='nombre_apellidos_id.carnet_identidad')
    historia_clinica = fields.Char(related='nombre_apellidos_id.historia_clinica')
    primer_apellido = fields.Char(related='nombre_apellidos_id.primer_apellido')
    segundo_apellido = fields.Char(related='nombre_apellidos_id.segundo_apellido')
    sexo = fields.Selection(related='nombre_apellidos_id.sexo')
    color_piel = fields.Selection(related='nombre_apellidos_id.color_piel')
    edad_actual = fields.Char(related='nombre_apellidos_id.edad_actual')
    calle = fields.Char(related='nombre_apellidos_id.calle')
    numero = fields.Char(related='nombre_apellidos_id.numero')
    entre_calles = fields.Char(related='nombre_apellidos_id.entre_calles')
    ciudad_o_pueblo = fields.Char(related='nombre_apellidos_id.ciudad_o_pueblo')
    provincia = fields.Selection(related='nombre_apellidos_id.provincia')
    nombre_apellidos_acomp = fields.Char(related='nombre_apellidos_id.nombre_apellidos_acomp')
    direccion_acomp = fields.Char(related='nombre_apellidos_id.direccion_acomp')
    telefono_acomp = fields.Char(related='nombre_apellidos_id.telefono_acomp')
    
    #@api.multi
    def confir_historia_clinic(self):
        self.write({'state_hist_clinic':'confir'})
    
    def cancel_historia_clinic(self):
        self.write({'state_hist_clinic':'cancel'})
        
    
    #usar esta funcion para validar valores
    #_sql_constraints = [
    #    (
    #        'check_amount_not_negative',
    #        'CHECK(amount >= 0.0)',
    #        "The payment amount cannot be negative.",
    #    ),
    #]
    
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