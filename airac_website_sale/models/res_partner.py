# -*- coding: utf-8 -*-
# © <2018> <Omar Torres (otorres@proogeeks.com)>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import fields, models, api

class ResPartner(models.Model):
    _inherit = 'res.partner'

    airac_user_product_ids = fields.Many2many(
        string='Productos Autorizados',
        comodel_name='product.product',
        relation='airac_website_product_customer',
        column1='customer_id',
        column2='product_id'
    )
