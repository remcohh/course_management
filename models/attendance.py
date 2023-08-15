from odoo import fields, models

class CmSession(models.Model):
    _name = "cm.attendance"
    _inherits = {"cm.registration": "registration"}
    registration = fields.Many2one("cm.registration")
    session = fields.Many2one("cm.session")
    present = fields.Boolean()
    