from odoo import fields, models


class OrderCategory(models.Model):
    _name = "order.meal.category"
    _description = "Order Meal Category"

    name = fields.Char("Name", required=True)


class Meal(models.Model):
    _name = 'order.meal'
    _description = "Order Meal"

    name = fields.Char("Name", required=True)
    price = fields.Float("Price", required=True)
    # ondelete = restrict | cascade | set null | no action | set default
    category_id = fields.Many2one('order.meal.category', string="Category", ondelete="cascade")
