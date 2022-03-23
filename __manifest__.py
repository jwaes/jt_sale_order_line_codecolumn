# -*- coding: utf-8 -*-
{
    'name': "jt_sale_order_line_codecolumn",

    'summary': "JT Sale order line product code column in report",

    'description': "",

    'author': "jaco tech",
    'website': "https://jaco.tech",
    "license": "AGPL-3",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Sales',
    'version': '15.0.1.0.1',

    # any module necessary for this one to work correctly
    'depends': ['sale'],

    # always loaded
    'data': [
        'report/sale_report_templates.xml',
    ],
}
