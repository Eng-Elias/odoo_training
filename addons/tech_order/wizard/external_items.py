from odoo import models, fields


import logging
_logger = logging.getLogger(__name__)


class ExternalItems(models.TransientModel):
    _name = "external.items"
    _description = "External Items"

    _transient_max_count = 3
    _transient_max_hours = 3

    external_item_ids = fields.Many2many('external.item', string="External Item")

    def add_external_items(self):
        order_id = self.env['meal.order'].browse(self.env.context.get('active_id'))
        _logger.error("feedback_id +++ " + str(order_id))
        order_id.external_item_ids = self.external_item_ids
