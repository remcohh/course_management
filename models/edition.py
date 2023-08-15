from odoo import fields, models

class Product(models.Model):
    _inherit = 'product.product'
    start_date = fields.Date()
    session_field_ids = fields.One2many('cm.session', 'product', string="session IDS")
    registration_field_ids = fields.One2many('cm.registration', 'product', string="registration IDS")
    