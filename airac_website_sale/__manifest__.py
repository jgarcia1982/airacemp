# -*- coding: utf-8 -*-
{
    'name': "AIRAC WEBSITE SALE",

    'summary': """AIRAC WEBSITE SALE""",

    'description': """

    """,

    'author': "Omar Torres",
    'website': "http://proogeeks.com",

    # Categories can be used to filter modules in modules listing
    'category': 'Sales',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['product','document','website','hr','sale','airac_hr','airac_sale','airac_inventory'],

    # always loaded
    'data': [
        'data/website_data.xml',
        'views/website_templates.xml',
        'views/res_partner.xml',
        'views/product_product.xml',
        'views/templates.xml',
    ],
    "post_init_hook": "post_init_hook"
}
