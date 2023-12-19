from odoo import fields, models, api

class ProductTemplate(models.Model):
    _inherit = 'product.template'
    stage = fields.Many2one('cm.product_stage', group_expand='_expand_stages')
    grading_profile = fields.Many2one('cm.grading_profile')
    
    def _expand_stages(self, states, domain, order):
        stage_ids = self.env['cm.product_stage'].search([])
        return stage_ids
    
    @api.model
    def price_range(self):        
        min_pricelist = self.env['product.pricelist'].search([('code', '=','Overig')])
        min_price = min_pricelist._get_product_price(self.product_variant_ids[0], quantity=1)
        max_pricelist = self.env['product.pricelist'].search([('code', '=','Aanmelder')])
        max_price = max_pricelist._get_product_price(self.product_variant_ids[0], quantity=1)
        return(f'from {min_price} until {max_price}')