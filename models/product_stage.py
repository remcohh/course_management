from odoo import fields, models

class CmProductStage(models.Model):
    _name = "cm.product_stage"
    name = fields.Char(String="Stage")
