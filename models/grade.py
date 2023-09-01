from odoo import fields, models

class CmGrade(models.Model):
    _name = "cm.grade"
    registration = fields.Many2one("cm.registration", ondelete='cascade')
    test = fields.Many2one("cm.test")
    grade = fields.Float()
    