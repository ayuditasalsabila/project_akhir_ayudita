# -*- coding: utf-8 -*-
# from odoo import http


# class Caferesto(http.Controller):
#     @http.route('/caferesto/caferesto/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/caferesto/caferesto/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('caferesto.listing', {
#             'root': '/caferesto/caferesto',
#             'objects': http.request.env['caferesto.caferesto'].search([]),
#         })

#     @http.route('/caferesto/caferesto/objects/<model("caferesto.caferesto"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('caferesto.object', {
#             'object': obj
#         })
