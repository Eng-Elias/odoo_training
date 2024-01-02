# -*- coding: utf-8 -*-
from datetime import datetime

from odoo import models, fields, api
from odoo.exceptions import ValidationError


class Material(models.Model):
    _name = "training.material"
    _description = "Training Material"

    name = fields.Char("Name", required=True)


class Teacher(models.Model):
    _name = "training.teacher"
    _description = "Teacher"

    name = fields.Char("Teacher", required=True)


class Course(models.Model):
    _name = "training.course"
    _description = "Training Course"

    name = fields.Char("Name", required=True)
    num_of_students = fields.Integer("Number of Students")
    material_ids = fields.Many2many("training.material", string="Materials")
    active = fields.Boolean(default=True)
    start_date = fields.Date("Start Date")
    end_date = fields.Date("End Date")
    duration = fields.Float("Duration")
    type = fields.Selection(
        [('online', 'Online'), ('onsite', 'Onsite')],
        string="Type"
    )
    responsible = fields.Many2one("training.teacher", string="Teacher", ondelete="set null")
    sessions_ids = fields.One2many("training.session", "course_id", "Course Sessions")


class Session(models.Model):
    _name = "training.session"
    _description = "Training Session"

    name = fields.Char("Name")
    planned_date = fields.Date("Planned Date")
    actual_date = fields.Date("Actual Date")
    course_id = fields.Many2one("training.course", "Course")

    @api.constrains('planned_date', 'actual_date')
    def check_session_dates(self):
        for record in self:
            if record.planned_date and record.actual_date and record.actual_date < record.planned_date:
                raise ValidationError("Actual Date must be equal to or after Planned Date")


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
