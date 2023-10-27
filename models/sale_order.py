from odoo import models

class SaleOrder(models.Model):
    _inherit = 'sale.order'
    
    def action_confirm(self):
        result = super(SaleOrder, self).action_confirm()
        student = self.env['cm.student'].create({"partner": self.partner_id.id, "state":"new"})
        for order_line in self.order_line:
            self.env['cm.registration'].create({"student": student.id, "product": order_line.product_id.id})            
        return result
    