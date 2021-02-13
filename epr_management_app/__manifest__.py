# -*- coding: utf-8 -*-
{
    'name': "ERP Management App",

    'summary': """
        ERP Management App""",

    'description': """
        ERP Management
    """,
    'depends': [],

    'author': "Wenzhuo Liang",
    'website': "todo",

    # for the full list
    'version': '0.1',

    # always loaded
    'data': [
        'views/purchase_order_view.xml',
        'security/ir.model.access.csv',
        'views/buyer.xml',
        'views/vendor.xml',
        'views/product.xml'
    ],
    # 'installable': True,
    'application': True
}