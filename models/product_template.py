from odoo import fields, models

class ProductTemplate(models.Model):
    _inherit = 'product.template'
    stage = fields.Many2one('cm.product_stage', group_expand='_expand_stages')
    
    def _expand_stages(self, states, domain, order):
        stage_ids = self.env['cm.product_stage'].search([])
        return stage_ids