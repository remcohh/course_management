from odoo import fields, models

class CmSession(models.Model):
    _name = "cm.attendance"
    _inherits = {"cm.registration": "registration"}
    registration = fields.Many2one("cm.registration", ondelete='cascade')
    session = fields.Many2one("cm.session", ondelete='cascade')
    present = fields.Boolean()
    