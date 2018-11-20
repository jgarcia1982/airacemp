# -*- coding: utf-8 -*-
# © <2018> <Omar Torres (otorres@proogeeks.com)>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

import logging

from odoo import api, fields, models

_logger = logging.getLogger(__name__)

class StockPicking(models.Model):
    _inherit = 'stock.picking'

    airac_ship_company_id = fields.Many2one(
        string='Compañía de Envío',
        comodel_name='res.company'
    )
    airac_delivery_guide = fields.Char(
        string='Numero de Guia',
        size=80
    )