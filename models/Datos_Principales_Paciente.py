# -*- coding: utf-8 -*-
from odoo import api, fields, models, _ 
from odoo.exceptions import UserError, ValidationError


#creando modelos (tablas de la base de datos) a partir de clases
# Datos Principales del Paciente 1er. modelo principal 
class Paciente(models.Model):
    _name = 'cad.paciente'
    _description = 'Contiene los datos principales de una persona natural'
    _rec_name='nombre' 
    
    
    image = fields.Binary(string='Foto del Paciente', help = 'Aquí va la foto del paciente')
    carnet_identidad = fields.Char(string='Carnet de Identidad', size = 11, required=True, help = "Va el número de carnet de Identidad de persona natural") #validar este campo
    #Datos del nombre de la persona natural
    nombre = fields.Char(string = 'Nombre(s)', size = 100, required = True) #validar este campo
    primer_apellido = fields.Char(string = '1er. Apellido', size = 100) #validar este campo
    segundo_apellido = fields.Char(string = '2do. Apellido', size = 100) #validar este campo
    #Datos del sexo
    sexo = fields.Selection(string='Sexo', selection=[('masculino', 'Masculino'), ('femenino', 'Femenino')])
    color_piel = fields.Selection(string='Color Piel', selection=[('blanca', 'Blanca'), ('negra', 'Negra'), ('amarilla', 'Amarilla'), ('mestiza', 'Mestiza')])
    edad_actual = fields.Integer(string = 'Edad', size = 3, required= True) #validar este campo
    
    #Datos de la dirección
    calle = fields.Char(string = 'Calle', size = 200)
    numero = fields.Char(string = 'Número')
    entre_calles = fields.Char(string = 'Entre calles')
    ciudad_o_pueblo = fields.Char(string = 'Ciudad o Pueblo')
    phone_movil = fields.Char(string = 'Móvil', size = 8)
    telefono_trabajo = fields.Char(string = 'Teléfono trabajo', size = 8)
    telefono_casa = fields.Char(string = 'Teléfono casa', size = 8)
    profesion = fields.Char(string = 'Profesión', size = 100)
    
    #Datos de la Provincia y Municipio 
    municipio_id = fields.Selection(string = 'Municipio', selection=[('santiago_cuba', 'Santiago de Cuba'), ('guama', 'Guama'), ('mella', 'Mella'), ('palma_soriano', 'Palma Soriano'), 
                                                                ('san_luis', 'San Luis'), ('contramaestre', 'Contramaestre'), ('songo_maya', 'Songo La Maya'), ('II_frente', 'II Frente'), ('III_frente', 'III Frente')])
    provincia = fields.Selection(string = 'Provincia', selection=[('guantanamo', 'Guantanamo'), ('santiago_cuba', 'Santiago de Cuba'), ('granma', 'Granma'), ('holguin', 'Holguin'), ('las_tunas', 'Las Tunas'), ('camaguey', 'Camaguey'),
                                                                ('ciego_avila', 'Ciego de Avila'), ('santi_spíritus', 'Santi Spíritus'), ('villa_clara', 'Villa Clara'), ('cienfuegos', 'Cienfuegos'), ('isla_juventud', 'Isla de la Juventud'), 
                                                                ('matanzas', 'Matanzas'), ('mayabeque', 'Mayabeque'), ('artemisa', 'Artemisa'), ('pinar_rio', 'Pinar del Rio'), ('la_habana', 'La habana')]) 
    #Datos del acompañante del paciente
    nombre_apellidos_acomp = fields.Char('Nombre y Apellidos Acompañante', size = 150)
    direccion_acomp = fields.Char(string = 'Direccion Acompañante', size = 250)
    telefono_acomp = fields.Char(string = 'Telefono Acompañante', size = 8)
    historia_clinica = fields.Char(string = 'Historia Clinica', required = True, size = 6, copy = False, help = 'Número de historia clínica') #validar este campo
    activo = fields.Boolean(string = 'Paciente activo', default = True, help = 'La edad del paciente debe estar entre 5 años <= edad <= 67 años')


    #-----------------------------------------------------------------------#
    #                            VALIDACIONES                               #
    #-----------------------------------------------------------------------#
    #Metódo que verifica que no se repitan valores
    
    #Validación de carnet de identidad
    _sql_constraints = [
        ('unique_h_clinic', 'unique(historia_clinica)', 'This numbers HC already exists'),
        ('unique_carnet_ident','unique(carnet_identidad)', 'El número de carnet identidad debe ser único.'),
        ('lenght_carnet_ident','CHECK (char_lenght(carnet_identidad) = 11)', 'El número de carnet identidad debe tener 11 dígitos.'),
        ('carnet_ident_format', 'CHECK (substring(carnet_identidad, 1, 6):: integer <= 999999 )', 'Los primeros 6 dígitos deben representar una fecha válida.'),
        ('carnet_ident_century','CHECK (substring(carnet_identidad, 7, 1):: integer >= 1 AND substring(carnet_identidad, 7, 1):: integer <= 9)', 'El séptimo dígito debe representar un siglo válido.')
    ]
#Datos del acompañante del paciente
#class Acompanante(models.Model):
#    _name = 'cad.acompanante'
#    _description = 'Contiene los datos de la persona acompañante'
#    _rec_name= 'nombre_apellidos'
    
#    nombre_y_apellidos =  fields.Char('Nombre y Apellidos', size = 150)
#    direccion = fields.Text(string = 'Direccion', size = 250)
#    telefono = fields.Integer(size = 8)    
    
          
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

#usar esta funcion para validar valores
    #_sql_constraints = [
    #    (
    #        'check_amount_not_negative',
    #        'CHECK(amount >= 0.0)',
    #        "The payment amount cannot be negative.",
    #    ),
    #]