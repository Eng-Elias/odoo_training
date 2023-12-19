from typing import Dict, List

from odoo import fields, models


class OrderCategory(models.Model):
    _name = "order.meal.category"
    _description = "Order Meal"

    name = fields.Char(string="Name", required=True)

    def onchange(self, values: Dict, field_names: List[str], fields_spec: Dict):
        pass


class OrderMeal(models.Model):
    _name = "order.meal"
    _description = "Order Meal"

    name = fields.Char(string="Name")
    price = fields.Float(string="Price")

    def onchange(self, values: Dict, field_names: List[str], fields_spec: Dict):
        pass
