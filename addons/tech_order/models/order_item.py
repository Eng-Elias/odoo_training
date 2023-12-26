from odoo import models, fields


class OrderItem(models.Model):
    _name = 'order.item'
    _description = 'Order Item'

    meal_id = fields.Many2one('order.meal', string="Meal", ondelete="restrict")  # restrict
    total_price = fields.Float(string='Total Price')
    quantity = fields.Float(string="Quantity")
    price = fields.Float("Price")
