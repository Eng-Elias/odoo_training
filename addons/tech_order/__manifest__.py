# -*- coding: utf-8 -*-
{
    'name': "Tech Order",

    'summary': """
        Food Order""",

    'description': """
        
    """,

    'author': "Tala",
    'website': "https://sy.linkedin.com/in/talah-hjaij",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'product'],

    # always loaded
    'data': [
            'security/security.xml',
            'security/ir.model.access.csv',
            'views/meal.xml',
            'wizard/feedback_reason.xml',
            'wizard/external_items.xml',
            'wizard/add_external_item.xml',
            'views/order.xml',
            'views/meal_ingredient.xml',
            'views/order_item.xml',
            'views/custome_feedback.xml',
            'data/server_action.xml',
            'data/scheduale_action.xml',

    ],

    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
