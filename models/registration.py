from odoo import fields, models, api
from datetime import datetime

class CmRegistration(models.Model):
    _name = "cm.registration"
    _description = "Registration model"
    _inherits = {"product.product": "product"}
    _rec_name = 'reg_title'
    product = fields.Many2one('product.product')
    student = fields.Many2one('cm.student', ondelete='cascade')
    reg_title = fields.Char(compute='_compute_fields_combination')
    attendance_ids = fields.One2many('cm.attendance', 'registration')
    grade_ids = fields.One2many('cm.grade', 'registration')
    average_grade = fields.Float(compute='_compute_average_grade', store=True)
    sessions_absent = fields.Integer(compute='_compute_sessions_absent', store=True)
    passed = fields.Boolean(compute='_compute_result', store=True)

    @api.depends('student', 'product')
    def _compute_fields_combination(self):
        for t in self:
            t.reg_title = t.student.name + ' / ' + t.product.name
            
    @api.model
    def create(self, vals):
        registration = super(CmRegistration, self).create(vals)
        sessions = self.env['cm.session'].search(
            [('product', '=', registration.product.id), ('date_time', '>', datetime.now().strftime('%Y-%m-%d 00:00:00'))])
        if sessions:
            for session in sessions:
                self.env['cm.attendance'].create({"registration": registration.id, "session": session.id})
                if session.test:
                    self.env['cm.grade'].create({"registration": registration.id, "session": session.id, "grade": 0})
        return registration
    
    @api.depends("grade_ids")
    def _compute_average_grade(self):
        if(len(self.grade_ids) == 0):
            return(0)
        for record in self:
              total_points = 0
              for grade in self.grade_ids:
                  total_points += grade.grade
              record.average_grade = total_points/len(self.grade_ids)
            
    @api.depends("attendance_ids")
    def _compute_sessions_absent(self):
        for record in self:
            sessions_absent = 0
            for attendance in self.attendance_ids:
                if not attendance.present: sessions_absent += 1
            record.sessions_absent = sessions_absent           
            
    @api.depends("average_grade", "sessions_absent")
    def _compute_result(self):
        for record in self:
            allowed_absence_sessions = self.grading_profile.allowed_absence_sessions            
            if(record.sessions_absent <= allowed_absence_sessions and record.average_grade >=5.5):
                record.passed = True
            else:
                record.passed = False