from odoo import fields, models

class CmTest(models.Model):
    _name = "cm.test"   
    _rec_name = 'title'
    product = fields.Many2one('product.product')
    title = fields.Char()
    description = fields.Html("description")
    