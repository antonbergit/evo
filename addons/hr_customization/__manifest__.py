# -*- coding: utf-8 -*-
{
    'name': "/tmp/hr_customization",

    'summary': "Short (1 phrase/line) summary of the module's purpose",

    'description': """
Long description of module's purpose
    """,

    'author': "My Company",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '1.9',

    # any module necessary for this one to work correctly
    'depends': ['base', 'hr', 'hr_recruitment', 'hr_skills', 'hr_contract'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/hr_employee_views.xml',
        'views/employee_position_views.xml',
        'views/organization_chart_template.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'employee_position/static/src/js/organization_chart.js',
        ],
    },
    # only loaded in demonstration mode
    'demo': [
        # 'demo/demo.xml',
    ],
    'application': True,
 	'installable': True,
}

