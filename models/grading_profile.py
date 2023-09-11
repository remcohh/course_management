from odoo import fields, models

class CmGradingProfile(models.Model):
    _name = "cm.grading_profile"
    product_templates = fields.One2many("product.template", "grading_profile")
    tests = fields.Many2many("cm.test")
    name = fields.Char()
    allowed_absence_sessions = fields.Integer()
    