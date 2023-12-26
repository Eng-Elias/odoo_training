from odoo import models, fields
from odoo.exceptions import ValidationError
from datetime import date, datetime, timedelta


class MealOrder(models.Model):
    _name='meal.order'
    _description='Meal Order'
    _order = 'name'

    name = fields.Char("Name", copy=False)
    type = fields.Selection([('internal','Internal'), ('external', 'External')],
                            string="Type", default="internal")

    order_date = fields.Date("Order Date", readonly=True, default=fields.datetime.now().date())
    total_price = fields.Float(string="Total Price", readonly=True, default=0)
    note = fields.Text("Note")
    expected_duration = fields.Float("Expected Duration")
    customer_id = fields.Many2one('res.partner', "Customer", ondelete='restrict')
    table_number = fields.Integer("Table Number")
    is_urgent = fields.Boolean("Is Urgent", copy=False)
    active = fields.Boolean(default=True)
    order_tag_ids = fields.Many2many('order.tag', "Tags")

    # order_tag_ids = fields.Many2many('order.tag',
    #                                  relation="Tags", column1='order', column2='tag')
