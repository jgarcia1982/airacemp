# -*- coding: utf-8 -*-
# © <2018> <Omar Torres (otorres@proogeeks.com)>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import fields, models, api

class airac_customer_sku(models.TransientModel):
    _name = 'airac.customer.sku'
    _description = 'AIRAC CUSTOMER SKU'

    product_id = fields.Many2one(
        string='Producto',
        comodel_name='product.template'
    )
    airac_sku_line_ids = fields.One2many(
        string='SKU Clientes',
        comodel_name='airac.sku.line',
        inverse_name='wizard_id'
    )

    @api.multi
    def prepare_wizard(self):

        wizard_id = self.create({
            'product_id': self.env.context.get('active_id', False)
        })

        self.env.cr.execute("""
            SELECT customer_id, customer_sku 
            FROM airac_website_product_customer
            WHERE product_id = %s
        """ % wizard_id.product_id.id)

        for line in self.env.cr.fetchall():

            self.env['airac.sku.line'].create({
                'wizard_id': wizard_id.id,
                'customer_id': line[0],
                'customer_sku': line[1]
            })

        return {
            'name': 'SKU Clientes',
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': self._name,
            'res_id': wizard_id.id,
            'type': 'ir.actions.act_window',
            'target': 'new',
            'context': self.env.context
        }

    @api.multi
    def update_customer_sku(self):

        self.ensure_one()

        update_query = ''

        for sku_line in self.airac_sku_line_ids:
            update_query += "UPDATE airac_website_product_customer "
            update_query += "SET customer_sku = '%s' WHERE customer_id = %s AND product_id = %s;" % (
                (sku_line.customer_sku or ' ').strip(),
                sku_line.customer_id.id,
                self.product_id.id
            )

        if update_query:
            self.env.cr.execute(update_query)