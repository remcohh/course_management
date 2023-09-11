from odoo import fields, models

class CmGrade(models.Model):
    _name = "cm.grade"
    _inherits = {"cm.session": "session", "cm.registration": "registration"}
    session = fields.Many2one("cm.session", ondelete='cascade')
    registration = fields.Many2one("cm.registration", ondelete='cascade')
    grade = fields.Float()
    