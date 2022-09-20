from odoo import api, fields, models, _


class ProductCategory(models.Model):
    _inherit = 'product.category'
    _sql_constraints = [
        ('unique_catalog_no', 'unique(catalog_no)', 'The catalog number must be unique!'),
    ]

    code = fields.Char()
    code_symbol = fields.Char()
    catalog_no = fields.Char()

    @api.onchange('parent_id', 'code_symbol')
    def _category_sequence(self):
        if self.parent_id and self.code_symbol:
            parent_code = self.parent_id.code
            total_categories = self.env['product.category'].search_count([('parent_id', '=', self.parent_id.id)])
            if total_categories > 0:
                self.code = parent_code + '-'  + '00' + str(total_categories + 1)
            else:
                self.code = parent_code + '-'  + '00' + str(1)
        elif self.code_symbol:
            self.code = self.code_symbol + '00' + str(1)
