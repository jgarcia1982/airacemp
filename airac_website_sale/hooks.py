# -*- coding: utf-8 -*-
# © <2018> <Omar Torres (otorres@proogeeks.com)>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

import logging

from odoo import api, tools, SUPERUSER_ID

_logger = logging.getLogger(__name__)

def post_init_hook(cr, registry):
    _order_website_sale_menus(cr, registry)


def _order_website_sale_menus(cr, registry):
    env = api.Environment(cr, SUPERUSER_ID, {})

    menu_table = env['website.menu']
    main_menus = menu_table.search([('url', '=', '/default-main-menu'), ('website_id', '!=', False)])

    for main_menu in main_menus:
        parent_menu = menu_table.search([('url', '=', '/customer_orders'), ('website_id', '=', main_menu.website_id.id)], limit=1)
        child_menus = menu_table.search([
            ('url', 'in', ('/customer_new_order','/customer_orders_state')),
            ('website_id', '=', main_menu.website_id.id)
        ])

        for child_menu in child_menus:
            child_menu.parent_path = '%s/%s/%s/' % (main_menu.id, parent_menu.id, child_menu.id)
            child_menu.parent_id = parent_menu.id