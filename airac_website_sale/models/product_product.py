# -*- coding: utf-8 -*-

from odoo import api, fields, models

class product_product(models.Model):
    _inherit = 'product.product'

    airac_sku_code = fields.Char(
        string='Airac SKU',
        size=50
    )