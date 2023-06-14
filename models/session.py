from odoo import fields, models, api

class CmSession(models.Model):
    _name = "cm.session"
    _inherits = {'product.product': 'product'}
    _rec_name = 'res_title'
    product = fields.Many2one("product.product")
    attendance_ids = fields.One2many('cm.attendance', 'session', string="attendance IDS")
    date_time = fields.Datetime()
    location = fields.Char()
    res_title = fields.Char(compute='_compute_fields_combination')

    @api.depends('date_time', 'product')
    def _compute_fields_combination(self):
        for t in self:
            t.res_title = t.date_time.strftime("%d-%m-%Y, %H:%M") + ' / ' + t.product.name

    