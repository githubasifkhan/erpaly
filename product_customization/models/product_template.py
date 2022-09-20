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
    description = fields.Char()

    @api.model
    def create(self, vals):
        if vals.get('identity', 'New') == 'New':
            vals['identity'] = self.env['ir.sequence'].next_by_code(
                'product.template') or 'New'
        result = super(ProductTemplate, self).create(vals)
        return result

    @api.onchange('categ_id', 'gsm')
    def _compute_description(self):
        for rec in self:
            if rec.categ_id and rec.gsm:
                if rec.categ_id.parent_id:
                    rec.description = rec.name + ' ' + str(rec.categ_id.parent_id.name) + ' - ' + str(
                        rec.gsm) + ' ' + 'GSM'
                else:
                    rec.description = rec.name + ' ' + str(rec.categ_id.name) + ' - ' + str(rec.gsm) + ' ' + 'GSM'
