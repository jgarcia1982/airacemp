# -*- coding: utf-8 -*-
{
    'name': "airac_report_quotation",

    'summary': """
        Agregar campo commitment_date al report Quotation""",

    'description': """
        Ventas 04
    """,

    'author': "Ideanet",
    'website': "http://www.ideanet.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'sale'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'report_commitment.xml'
    ],
}
