# -*- coding: utf-8 -*-
{
    'name': "AIRAC INVENTORY",

    'summary': """AIRAC INVENTORY""",

    'description': """

    """,

    'author': "Omar Torres",
    'website': "http://proogeeks.com",

    # Categories can be used to filter modules in modules listing
    'category': 'Warehouse',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['stock'],

    # always loaded
    'data': [
        'data/inventory_data.xml',
        'views/stock_picking.xml'
    ]
}
