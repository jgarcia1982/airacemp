# -*- coding: utf-8 -*-

from odoo import api, fields, models

class airac_website_product_customer(models.Model):
    _name = 'airac.website.product.customer'

    product_id = fields.Many2one(
        string='Producto',
        comodel_name='product.template'
    )
    customer_id = fields.Many2one(
        string='Cliente',
        comodel_name='res.partner'
    )
    customer_sku = fields.Char(
        string='SKU Cliente',
        size=80
    )