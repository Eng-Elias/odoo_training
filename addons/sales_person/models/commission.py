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


class CommissionLine(models.Model):
    _name = 'sales_person.commission.line'
    _description = 'Sales Person Commission Line'

    commission_id = fields.Many2one('sales_person.commission', string="Commission", required=True)
    from_value = fields.Float(string="From Value", required=True)
    to_value = fields.Float(string="To Value", required=True)
    percentage = fields.Float(string="Percentage", required=True)


class CommissionLineProduct(models.Model):
    _name = 'commission.line.product'
    _description = 'Sales Person Commission Line Product'

    _rec_name = 'product_id'

    commission_line_id = fields.Many2one('sales_person.commission.line', string="Commission Line Product", required=True)
    product_id = fields.Many2one('product.product', 'Product', ondelete="restrict")
