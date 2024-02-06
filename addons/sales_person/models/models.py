# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class sales_person(models.Model):
#     _name = 'sales_person.sales_person'
#     _description = 'sales_person.sales_person'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

