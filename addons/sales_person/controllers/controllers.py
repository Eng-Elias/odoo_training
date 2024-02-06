# -*- coding: utf-8 -*-
# from odoo import http


# class SalesPerson(http.Controller):
#     @http.route('/sales_person/sales_person', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sales_person/sales_person/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('sales_person.listing', {
#             'root': '/sales_person/sales_person',
#             'objects': http.request.env['sales_person.sales_person'].search([]),
#         })

#     @http.route('/sales_person/sales_person/objects/<model("sales_person.sales_person"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sales_person.object', {
#             'object': obj
#         })

