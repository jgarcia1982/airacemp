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
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['documents','website_sale_digital','airac_sale','airac_inventory','airac_hr'],

    # always loaded
    'data': [
        'data/website_data.xml',
        'views/website_templates.xml',
        'views/res_partner.xml',
        'views/product_product.xml',
    ],
    "post_init_hook": "post_init_hook"
}
