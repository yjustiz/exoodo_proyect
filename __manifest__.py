 # -*- coding: utf-8 -*-
{
    'name': "Centro Atención Diabeticos",

    'summary': """
        NUEVO
        """,

    'description': """
        Va un resumen sobre el modulo y sus funciones
    """,

    'author': "Yordan Justiz Madrigal",
    'website': "yordanjustiz86@gmail.com",
    'Company': "EXOODO",
    
    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['base'],
    
    'installable': True,
    
    'application': True,

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'data/sequenc.xml',
        'views/Programacion_Turnos.xml',
        'views/historia_clinica.xml',
        'views/Datos_Principales_Paciente.xml',
        'views/menu.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
