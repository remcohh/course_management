from odoo import fields, models

class CmRegistration(models.Model):
    _name = "cm.registration"
    _description = "Registration model"
    _inherits = {"product.product": "product"}
    product = fields.Many2one('product.product')
    student = fields.Many2one('cm.student')
    status = fields.Selection([('Not started', 'Not started')])

