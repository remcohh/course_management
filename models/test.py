from odoo import fields, models

class CmTest(models.Model):
    _name = "cm.test"   
    _rec_name = 'title'
    grading_profiles = fields.Many2many("cm.grading_profile")
    title = fields.Char()
    description = fields.Html("description")
