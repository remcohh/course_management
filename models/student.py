from odoo import fields, models

class CmStudent(models.Model):
    _name = "cm.student"
    _inherits = {'res.partner': 'partner'}
    _inherit = 'mail.thread'
    student_type = fields.Selection([('Bachelor', 'Bachelor'),('Master', 'Master'),('Medewerker', 'Medewerker'), ('Extern', 'Extern')])
    partner = fields.Many2one('res.partner')
    registration_ids = fields.One2many('cm.registration', 'student')

