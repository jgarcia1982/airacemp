# -*- coding: utf-8 -*-
{
    'name': "AIRAC SALE",

    'summary': """AIRAC SALE""",

    'description': """

    """,

    'author': "Omar Torres",
    'website': "http://proogeeks.com",

    # Categories can be used to filter modules in modules listing
    'category': 'Sales',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['sale_management'],

    # always loaded
    'data': [
        'views/sale_order.xml'
    ]
}
