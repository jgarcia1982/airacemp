# -*- coding: utf-8 -*-
# © <2018> <Omar Torres (otorres@proogeeks.com)>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import fields, models, api

class airac_sku_line(models.TransientModel):
    _name = 'airac.sku.line'

    wizard_id = fields.Many2one(
        string='Wizard',
        comodel_name='airac.customer.sku'
    )
    customer_id = fields.Many2one(
        string='Cliente',
        comodel_name='res.partner'
    )
    customer_sku = fields.Char(
        string='SKU Cliente',
        size=80
    )