# -*- coding: utf-8 -*-

from odoo import models, fields


class Material(models.Model):
    _name = "training.material"
    _description = "Training Material"

    name = fields.Char("Name", required=True)


class Course(models.Model):
    _name = "training.course"
    _description = "Training Course"

    name = fields.Char("Name", required=True)
    num_of_students = fields.Integer("Number of Students")
    material_id = fields.Many2one("training.material", string="Material", ondelete="set null")


# class training(models.Model):
#     _name = 'training.training'
#     _description = 'training.training'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
