import re
from odoo import api, fields, models, _

class ProductTemplate(models.Model):
    _inherit = "product.template"

    short_name = fields.Char(compute='_compute_short_name', string='short_name')
    
    @api.depends('display_name')
    def _compute_short_name(self):
        for record in self:
            result = re.search(r'^(\[.*\]\s)*(.*)$', record.display_name)
            short = result.group(2)
            record.short_name = short