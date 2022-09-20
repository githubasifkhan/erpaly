# -*- coding: utf-8 -*-
{
    'name': "Product Customization",

    'summary': """
        This module is used to customize product category and product template.""",

    'description': """
        This module is used to customize product category and product template.
    """,

    'author': "Hassan Raza",


    'category': 'Uncategorized',
    'version': '15.0.1.0.0',
    'depends': ['stock', 'product'],
    'data': [
        'views/product_category_view.xml',
        'views/product_template_view.xml',
        'data/product_identity.xml',
    ],
}
