# -*- coding: utf-8 -*-
# from odoo import http


# class Quanlybanhang2222(http.Controller):
#     @http.route('/quanlybanhang2222/quanlybanhang2222', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/quanlybanhang2222/quanlybanhang2222/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('quanlybanhang2222.listing', {
#             'root': '/quanlybanhang2222/quanlybanhang2222',
#             'objects': http.request.env['quanlybanhang2222.quanlybanhang2222'].search([]),
#         })

#     @http.route('/quanlybanhang2222/quanlybanhang2222/objects/<model("quanlybanhang2222.quanlybanhang2222"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('quanlybanhang2222.object', {
#             'object': obj
#         })

