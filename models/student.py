from odoo import fields, models

class CmStudent(models.Model):
    _name = "cm.student"
    _inherits = {'res.partner': 'partner'}
    student_type = fields.Selection([('Bachelor', 'Master')])
    partner = fields.Many2one('res.partner')
