# -*- coding: utf-8 -*-
# © <2018> <Omar Torres (otorres@proogeeks.com)>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

import logging

from odoo import api, fields, models

_logger = logging.getLogger(__name__)

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    airac_production_state = fields.Selection(
        string='Estado producción',
        size=1,
        selection=[
            ('P', 'En Producción'),
            ('R', 'Terminado')
        ]
    )
    airac_stock_prod_id = fields.Many2one(
        string='Entrada de inventario',
        comodel_name='stock.picking'
    )
    commitment_date = fields.Datetime(
        string='Fecha de entrega compromiso'
    )
    state = fields.Selection(
        string='Estado',
        selection=[
            ('draft', 'Abierto'),
            ('sent', 'Presupuesto enviado'),
            ('sale', 'Confirmado'),
            ('production', 'En Producción'),
            ('ready', 'Terminado'),
            ('done', 'Bloqueado'),
            ('cancel', 'Cancelado'),
        ]
    )

    STATE_MAP = {
        'draft': 'Abierto',
        'sent': 'Presupuesto enviado',
        'sale': 'Confirmado',
        'production': 'En Producción',
        'ready': 'Terminado',
        'done': 'Bloqueado',
        'cancel': 'Cancelado'
    }

    def airac_web_state(self):
        self.ensure_one()

        if self.airac_production_state == 'P':
            return self.STATE_MAP['production']

        if self.airac_production_state == 'R':
            return self.STATE_MAP['ready']

        return self.STATE_MAP[self.state]

    @api.multi
    def action_so_production(self):
        self.ensure_one()
        self.airac_production_state = 'P'

    @api.multi
    def action_so_end(self):
        self.ensure_one()

        picking_type = self.env.ref('airac_inventory.airac_stock_type_production')
        picking_seq = self.env.ref('airac_inventory.airac_production_sequence')
        stock_location = self.env.ref('stock.location_production')
        picking_id = self.env['stock.picking'].create({
            'partner_id': self.company_id.partner_id.id,
            'picking_type_id': picking_type.id,
            'location_id': stock_location.id,
            'location_dest_id': picking_type.default_location_dest_id.id
        })

        for so_line in self.order_line:

            if so_line.product_id.type != 'product':
                continue

            move_id = self.env['stock.move'].create({
                'name': picking_seq._next(),
                'picking_id': picking_id.id,
                'product_id': so_line.product_id.id,
                'product_uom_qty': so_line.product_uom_qty,
                'quantity_done': so_line.product_uom_qty,
                'product_uom': so_line.product_uom.id,
                'location_id': stock_location.id,
                'location_dest_id': picking_id.location_dest_id.id,
            })

        picking_id.action_done()

        self.airac_stock_prod_id = picking_id.id
        self.airac_production_state = 'R'