from odoo import fields, models

class CmTeacher(models.Model):
    _name = "cm.skill"
    name = fields.Char(String="Skill")
