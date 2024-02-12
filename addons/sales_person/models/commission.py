from odoo import models, fields, api, exceptions


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

    @api.constrains('from_value', 'to_value')
    def check_overlap(self):
        for record in self:
            domain = [('id', '!=', record.id),
                      ('commission_id', '=', record.commission_id.id),
                      '|',
                      '&', ('from_value', '>=', record.from_value), ('from_value', '<=', record.to_value),
                      '&', ('to_value', '>=', record.from_value), ('to_value', '<=', record.to_value)]
            overlapping_lines = self.search(domain)
            if overlapping_lines:
                raise exceptions.ValidationError("Ranges cannot overlap in commission lines.")


class CommissionLineProduct(models.Model):
    _name = 'commission.line.product'
    _description = 'Sales Person Commission Line Product'

    _rec_name = 'product_id'

    commission_line_id = fields.Many2one('sales_person.commission.line', string="Commission Line Product", required=True)
    product_id = fields.Many2one('product.product', 'Product', ondelete="restrict")
