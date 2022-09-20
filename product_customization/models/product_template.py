from odoo import api, fields, models, _


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    item_group = fields.Char(related='categ_id.code', string='Item Group')
    catalog_no = fields.Char(related='categ_id.catalog_no')
    gsm = fields.Integer('GSM')
    width = fields.Integer('Width')
    length = fields.Integer('Length')
    quality = fields.Integer('Quality')
    identity = fields.Char(default='New')

    @api.model
    def create(self, vals):
        if vals.get('identity', 'New') == 'New':
            vals['identity'] = self.env['ir.sequence'].next_by_code(
                'product.template') or 'New'
        result = super(ProductTemplate, self).create(vals)
        return result

