from odoo import models, fields


class Commission(models.Model):
    _name = 'sales_person.commission'
    _description = "Sales Person Commission"

    from_date = fields.Date("From Date", required=True)
    to_date = fields.Date("To Date", required=True)
    target = fields.Selection([('quantity','quantity'), ('price','price'),], string="Target", required=True)
    state = fields.Selection([('draft', 'Draft'), ('confirmed', 'Confirmed'), ('rejected', 'Rejected')],
                             default='draft', string="State", readonly=True)

    def action_confirm(self):
        self.state = 'confirmed'

    def action_rejected(self):
        self.state = 'rejected'
