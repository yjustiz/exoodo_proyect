# -*- coding: utf-8 -*-
from odoo import api, fields, models 
from odoo.exceptions import ValidationError


#creando modelos (tablas de la base de datos) a partir de clases
# Datos Principales del Paciente 1er. modelo principal 
class Paciente(models.Model):
    _name = 'cad.paciente'
    _description = 'Contiene los datos principales de una persona natural'
    _rec_name='nombre' 
    
    image = fields.Binary(string='Foto del Paciente')
    carnet_identidad = fields.Char(string='Carnet de Identidad', size = 11, required=True, help = "Va el número de carnet de Identidad de persona natural") #validar este campo
    nombre = fields.Char(string = 'Nombre(s)', size = 50, required = True)
    primer_apellido = fields.Char(string = '1er. Apellido', size = 50)
    segundo_apellido = fields.Char(string = '2do. Apellido', size = 50)
    sexo = fields.Selection(string='Sexo', selection=[('masculino', 'Masculino'), ('femenino', 'Femenino')])
    color_piel = fields.Selection(string='Color Piel', selection=[('blanca', 'Blanca'), ('negra', 'Negra'), ('amarilla', 'Amarilla'), ('mestiza', 'Mestiza')])
    edad_actual = fields.Char(string = 'Edad', size = 3, required= True)
    calle = fields.Char(string = 'Calle', size = 200)
    numero = fields.Char(string = 'Número')
    entre_calles = fields.Char(string = 'Entre calles')
    ciudad_o_pueblo = fields.Char('Ciudad o Pueblo')
    telefono_trabajo = fields.Integer()
    telefono_casa = fields.Integer()
    profesion = fields.Char(string='Profesión', size = 100)
    municipio = fields.Selection(string='Municipio', selection=[('santiago de cuba', 'Santiago de Cuba'), ('guama', 'Guama'), 
                        ('mella', 'Mella'), ('palma soriano', 'Palma Soriano'),
                        ('san luis', 'San Luis'), ('contramaestre', 'Contramaestre'),
                        ('songo la maya', 'Songo La Maya'), ('II frente', 'II Frente'), 
                        ('III frente', 'III Frente')], default = 'Santiago de Cuba')
    provincia = fields.Selection(string='Provincia',  selection=[('guantanamo', 'Guantanamo'), ('santiago de cuba', 'Santiago de Cuba'),
                        ('granma', 'Granma'), ('holguin', 'Holguin'), ('las tunas', 'Las Tunas'), ('camaguey', 'Camaguey'),
                        ('ciego de avila', 'Ciego de Avila'), ('santi spíritus', 'Santi Spíritus'),
                        ('villa clara', 'Villa Clara'), ('cienfuegos', 'Cienfuegos'), ('isla de la juventud', 'Isla de la Juventud'), 
                        ('matanzas', 'Matanzas'), ('mayabeque', 'Mayabeque'), ('artemisa', 'Artemisa'),  
                        ('pinar del rio', 'Pinar del Rio'), ('la habana', 'La habana')], default = 'Santiago de Cuba') 
    nombre_apellidos_acomp =  fields.Char('Nombre y Apellidos Acompañante', size = 150)
    direccion_acomp = fields.Char(string = 'Direccion Acompañante', size = 250)
    telefono_acomp = fields.Char(string='Telefono Acompañante',size = 8)
    historia_clinica = fields.Char(string='Historia Clinica', required = True,size =5, help = 'Número de historia clínica') #validar este campo


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
