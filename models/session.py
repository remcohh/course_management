from odoo import fields, models, api
import pytz

class CmSession(models.Model):
    _name = "cm.session"
    _inherits = {'product.product': 'product'}
    _rec_name = 'res_title'
    product = fields.Many2one("product.product")
    teacher = fields.Many2one("cm.teacher")
    location = fields.Many2one("cm.location")
    attendance_ids = fields.One2many('cm.attendance', 'session', string="attendance IDS")
    date_time = fields.Datetime()
    res_title = fields.Char(compute='_compute_fields_combination')
    test = fields.Many2one('cm.test')
    grades = fields.One2many('cm.grade', 'session', string="attendance IDS")

    @api.depends('date_time', 'product')
    def _compute_fields_combination(self):
        for t in self:
            tz_name =self.env.user.tz
            context_tz = pytz.timezone(tz_name)
            t.res_title =pytz.utc.localize(t.date_time, is_dst=False).astimezone(context_tz).strftime("%d-%m-%Y, %H:%M")  + ' - ' + t.name
                        
    @api.model
    def create(self, vals):
        session = super(CmSession, self).create(vals)
        registrations = self.env['cm.registration'].search(
            [('product', '=', session.product.id)])
        if registrations:
            AttendanceModel = self.env['cm.attendance']
            attendance_records = []
            for registration in registrations:
                attendance_records.append(AttendanceModel.create(
                    {"registration": registration.id, "session": session.id}))
            if session.test:
                for registration in registrations:
                    self.env['cm.grade'].create(
                    {"registration": registration.id, "session": session.id, "grade": 0})            
        return session

    def write(self, vals):
        if(vals.get("test") == False):
            self._remove_grades()
        elif(self.test.id == False and vals.get("test", 0) > 0): 
            self._create_grades()   
        elif(vals.get("test", 0) > 0 and self.test.id != vals.get("test", 0)): 
            self._update_grades()            
        super(CmSession, self).write(vals)
        
    def _remove_grades(self):
        to_remove = self._linked_grades()
        to_remove.sudo().unlink()
        
    def _create_grades(self):
        registrations = self.env['cm.registration'].search([('product', '=', self.product.id)])
        for registration in registrations:
            self.env['cm.grade'].create({"registration": registration.id, "session": self.id, "grade": 0})    
        
    def _update_grades(self):
        grades_to_update = self._linked_grades()
        for grade in grades_to_update:
            grade.write({"test": self.test.id})
        
    def _linked_grades(self):            
        return(self.env['cm.grade'].search([('session', '=', self.id)]))