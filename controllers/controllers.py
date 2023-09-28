# -*- coding: utf-8 -*-
# from odoo import http


# class CentroAtencionDiabeticos(http.Controller):
#     @http.route('/centro__atencion__diabeticos/centro__atencion__diabeticos/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/centro__atencion__diabeticos/centro__atencion__diabeticos/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('centro__atencion__diabeticos.listing', {
#             'root': '/centro__atencion__diabeticos/centro__atencion__diabeticos',
#             'objects': http.request.env['centro__atencion__diabeticos.centro__atencion__diabeticos'].search([]),
#         })

#     @http.route('/centro__atencion__diabeticos/centro__atencion__diabeticos/objects/<model("centro__atencion__diabeticos.centro__atencion__diabeticos"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('centro__atencion__diabeticos.object', {
#             'object': obj
#         })
