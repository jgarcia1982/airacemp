# -*- coding: utf-8 -*-

from odoo import api, fields, models

class product_product(models.Model):
    _inherit = 'product.product'

    airac_web_customer_ids = fields.Many2many(
        string='Clientes',
        comodel_name='res.partner',
        relation='airac_website_product_customer',
        column1='product_id',
        column2='customer_id'
    )

    def airac_customer_sku(self, partner_id):

        self.env.cr.execute("""
            SELECT customer_sku
            FROM airac_website_product_customer
            WHERE product_id = %s AND customer_id = '%s'
        """ % (self.id, partner_id))
        result = self.env.cr.fetchone()

        return (result[0] or ' ').strip() if len(result) > 0 else ''