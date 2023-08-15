from odoo import fields, models, api
class CmRegistration(models.Model):
    _name = "cm.registration"
    _description = "Registration model"
    _inherits = {"product.product": "product"}
    _rec_name = 'reg_title'
    product = fields.Many2one('product.product')
    student = fields.Many2one('cm.student')
    status = fields.Selection([('Not started', 'Not started')])
    reg_title = fields.Char(compute='_compute_fields_combination')
    attendance_ids = fields.One2many('cm.attendance', 'registration')
    grade_ids = fields.One2many('cm.grade', 'registration')

    @api.depends('student', 'product')
    def _compute_fields_combination(self):
        for t in self:
            t.reg_title = t.student.name + ' / ' + t.product.name

