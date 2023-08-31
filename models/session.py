from odoo import fields, models, api

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
    completed = fields.Boolean()

    @api.depends('date_time', 'product')
    def _compute_fields_combination(self):
        for t in self:
            t.res_title = t.date_time.strftime("%d-%m-%Y, %H:%M") + ' / ' + t.product.name
            
            
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
        return session

    