from odoo import api, fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    max_table_number = fields.Integer(string="Max Table Number")