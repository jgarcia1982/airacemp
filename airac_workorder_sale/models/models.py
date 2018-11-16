# -*- coding: utf-8 -*-

from odoo import models, fields

class SaleOrder(models.Model):
    _name = "sale.order"
    _inherit = 'sale.order'

    x_workorder = fields.Char(string='Orden de Trabajo', required=False, default='', help='Este campo es para definir el numero de Orden de Trabajo en Manufactura para el pedido en cuestion')