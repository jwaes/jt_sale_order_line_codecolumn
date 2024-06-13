import re
from odoo import api, fields, models, _

class ProductProduct(models.Model):
    _inherit = "product.product"

    short_name = fields.Char(compute='_compute_short_name', string='short_name')
    
    @api.depends('display_name')
    def _compute_short_name(self):
        for record in self:
            result = re.search(r'^([.*]\s)*(.*)$', record.display_name)
            short = result.group(2)
            record.short_name = short    

    def get_product_multiline_description_sale(self):
        """ Compute a multiline description of this product, in the context of sales
                (do not use for purchases or other display reasons that don't intend to use "description_sale").
            It will often be used as the default description of a sale order line referencing this product.
        """
        name = self.short_name
        if self.description_sale:
            name += '\n' + self.description_sale

        return name
