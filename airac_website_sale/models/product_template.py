# -*- coding: utf-8 -*-

from odoo import api, fields, models

class product_template(models.Model):
    _inherit = 'product.template'

    airac_sku_code = fields.Char(
        string='Airac SKU',
        size=50
    )
    airac_web_customer_ids = fields.Many2many(
        string='Clientes',
        comodel_name='res.partner',
        relation='airac_website_product_customer',
        column1='product_id',
        column2='customer_id'
    )