# -*- coding: utf-8 -*-
{
    'name': "Onchange Pricelist Update Order Lines",

    'summary': """Auto Update the sale order lines when pricelist is changed""",

    'description': """Auto Update the sale order lines when pricelist is changed""",

    'author': 'ErpMstar Solutions',
    'category': 'Sale',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['sale_management'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'application': True,
    'images': ['static/description/pricelist_change.gif'],
    'website': '',
    'auto_install': False,
    'price': 25,
    'currency': 'EUR',
}
