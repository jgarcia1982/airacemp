# -*- coding: utf-8 -*-

import logging
import base64

from odoo import http
from odoo.http import request
from odoo.addons.web.controllers.main import content_disposition

_logger = logging.getLogger(__name__)

class WebsiteSale(http.Controller):

    @http.route('/customer_new_order', type='http', auth="user", website=True)
    def new_sale_order(self, **kw):

        user_id = http.request.env['res.users'].browse([http.request.env.uid])

        return http.request.render('airac_website_sale.website_new_sale_order_template', {
            'product_ids': user_id.partner_id.airac_user_product_ids
        })

    @http.route('/customer_orders_state', type='http', auth="user", website=True)
    def sale_order_state(self, **kw):

        user_id = http.request.env['res.users'].browse([http.request.env.uid])
        partner_id = user_id.partner_id
        child_ids = http.request.env['res.partner'].search([('parent_id', '=', partner_id.id)])
        customer_ids = [child_id.id for child_id in child_ids]
        customer_ids.append(partner_id.id)
        order_ids = http.request.env['sale.order'].sudo().search([
            ('partner_id', 'in', customer_ids),
            ('state', 'in', ['order','sale'])
        ])

        return http.request.render('airac_website_sale.website_sale_order_state_template', {
            'order_ids': order_ids
        })

    @http.route('/airac/update_order_values', type='http', auth="user", csrf=False)
    def update_order_values(self, **kw):

        subtotal = 0
        taxes = 0
        total = 0
        index = 0
        qty = kw['qty'].split(',')

        for product_id in http.request.env['product.product'].sudo().search([('id', 'in', kw['ids'].split(','))]):

            prod_subtotal = product_id.sudo().lst_price * float(qty[index])
            prod_taxes = prod_subtotal * (sum([tax_id.sudo().amount for tax_id in product_id.sudo().taxes_id]) / 100.0)

            subtotal += prod_subtotal
            taxes += prod_taxes
            total += prod_subtotal + prod_taxes

            index += 1

        return """{"subtotal": "%s", "taxes": "%s","total": "%s"}""" % (
            '{:0,.2f}'.format(subtotal),
            '{:0,.2f}'.format(taxes),
            '{:0,.2f}'.format(total)
        )

    @http.route('/airac/create_sale_order', type='http', auth="user", csrf=False)
    def create_sale_order(self, **kw):

        user_id = http.request.env['res.users'].browse([http.request.env.uid])
        qty = kw['qty'].split(',')
        index = 0

        order_id = http.request.env['sale.order'].sudo().create({
            'partner_id': user_id.partner_id.id,
            'client_order_ref': kw['customer_so_ref'].strip()
        })

        if 'file' in kw.keys():

            ctx = http.request._context.copy()
            ctx.pop('default_type', False)
            attachment_id = http.request.env['ir.attachment'].with_context(ctx).sudo().create({
                'name': kw['file'].filename,
                'res_id': order_id.id,
                'res_model': order_id._name,
                'datas': base64.b64encode(kw['file'].stream.read()),
                'datas_fname': kw['file'].filename,
                'description': 'Web Sale Order Attachement',
            })

        for product_id in kw['ids'].split(','):

            http.request.env['sale.order.line'].sudo().create({
                'product_id': int(product_id),
                'product_uom_qty': float(qty[index]),
                'order_id': order_id.id
            })

            index += 1

        return order_id.name