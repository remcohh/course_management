from odoo import fields, models

class CmSession(models.Model):
    _name = "cm.session"
    _inherits = {'product.product': 'product'}
    product = fields.Many2one("product.product")
    date_time = fields.Datetime()
    location = fields.Char()
    