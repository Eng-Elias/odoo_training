from odoo import models, fields


class CommissionPartner(models.Model):
    _name = 'commission.partner'
    _description = 'Commission Partner'

    _rec_name = 'partner_id'

    commission_id = fields.Many2one('sales_person.commission', string="Commission", ondelete='restrict', required=True)
    partner_id = fields.Many2one('res.partner', string="Partner", ondelete='restrict', required=True)
