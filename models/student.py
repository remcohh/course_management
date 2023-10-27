from odoo import fields, models, api

class CmStudent(models.Model):
    _name = "cm.student"
    _inherits = {'res.partner': 'partner'}
    _inherit = 'mail.thread'
    student_type = fields.Selection([('Bachelor', 'Bachelor'),('Master', 'Master'),('Medewerker', 'Medewerker'), ('Extern', 'Extern')])
    state = fields.Selection([('new', 'Nieuw'), ('verified', 'Geverifieerd')], default='new', string="Status")
    partner = fields.Many2one('res.partner')
    registration_ids = fields.One2many('cm.registration', 'student')
    
    def unlink(self):
        self.partner.unlink()   
        