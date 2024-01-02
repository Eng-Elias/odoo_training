from odoo import models, fields, api
from odoo.exceptions import ValidationError
from datetime import date, datetime, timedelta


class MealOrder(models.Model):
    _name='meal.order'
    _description='Meal Order'
    _order = 'name'

    name = fields.Char("Name", copy=False)
    type = fields.Selection([('internal', 'Internal'), ('external', 'External')],
                            string="Type", default="internal")

    order_date = fields.Date("Order Date", readonly=True, default=fields.datetime.now().date())
    expected_date = fields.Date("Expected Date", compute="_compute_expected_date")
    total_price = fields.Float(string="Total Price", readonly=True, default=0)
    note = fields.Text("Note")
    expected_duration = fields.Float("Expected Duration")
    customer_id = fields.Many2one('res.partner', "Customer", ondelete='restrict')
    table_number = fields.Integer("Table Number")
    is_urgent = fields.Boolean("Is Urgent", copy=False)
    active = fields.Boolean(default=True)
    order_tag_ids = fields.Many2many('order.tag', "Tags")
    item_ids = fields.One2many('order.item', 'order_id', string="Items")

    # order_tag_ids = fields.Many2many('order.tag',
    #                                  relation="Tags", column1='order', column2='tag')

    state = fields.Selection([('draft', 'Draft'),
                              ('confirmed', 'Confirmed'),
                              ('in_process', 'In Process'),
                              ('delivered', 'Delivered'),
                              ('cancelled', 'Cancelled'),
                              ],
                             string="State", default='draft')

    _sql_constraints = [
            ('unique_name', 'unique (name)', 'Order Name already exists!'),
            ]

    @api.constrains('order_date')
    def check_order_date(self):
        if self.order_date and self.order_date > datetime.now().date():
            raise ValidationError("Order Date Must be in present or past")

    def action_confirm(self):
        self.state = 'confirmed'

    def action_in_process(self):
        self.state = 'in_process'

    def action_delivered(self):
        self.state = 'delivered'

    def action_cancelled(self):
        self.state = 'cancelled'

    @api.depends("order_date", "expected_duration")
    def _compute_expected_date(self):
        for record in self:
            record.expected_date = record.order_date + timedelta(days=record.expected_duration)


        #Draft --> Confirm, Cancel
        #Confirm --> In Process, Cancel
        #In Process --> Delivered
        #Delivered --> X
