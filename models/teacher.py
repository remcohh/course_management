from odoo import fields, models, api

class CmTeacher(models.Model):
    _name = "cm.teacher"
    _inherits = {'res.partner': 'partner'}
    _inherit = 'mail.thread'
    _rec_name = 'teacher_title'
    partner = fields.Many2one('res.partner')
    skill = fields.Many2many('cm.skill')
    teacher_title = fields.Char(compute='_compute_fields_combination')
    
    @api.depends('partner')
    def _compute_fields_combination(self):
        for teacher in self:
            teacher.teacher_title = teacher.partner.name + ' (' + " ".join([skill.name for skill in teacher.skill]) + ')'