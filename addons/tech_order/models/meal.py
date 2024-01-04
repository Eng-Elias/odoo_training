from odoo import fields, models


class OrderMealCategory(models.Model):
    _name = 'order.meal.category'
    _description = "Order Meal Category"

    name = fields.Char("Name", required=True)


class Meal(models.Model):
    _name = 'order.meal'
    _description = "Order Meal"

    name = fields.Char("Name", required=True)
    price = fields.Float("Price", required=True)
    # ondelete = restrict | cascade | set null | no action | set default
    category_id = fields.Many2one('order.meal.category', string="Category", ondelete="cascade")
    ingredient_ids = fields.One2many('meal.ingredient', 'meal_id', string="Ingredient")
    feedback_ids = fields.One2many('customer.feedback', 'meal_id', string="feedbacks")


    def action_view_feedback(self):
        return {'type': 'ir.actions.act_window',
                'name': 'Feedback',
                'view_mode': 'tree',
                'res_model': 'customer.feedback',
                'target': 'current',
                'domain':[('id', 'in', self.feedback_ids.ids)],

                'context':{'default_meal_id':self.id}
                # 'context': {'create': True, 'default_meal_id': self.id}
                }
#self.feedback_ids.ids == [1,4,5]

# price ==> , store=False
# #select price from order_meal; -->X
# #[('price', '=', 500)]
#self.price
