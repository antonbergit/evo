# -*- coding: utf-8 -*-
{
    #  TODO: name it proper way
    'name': "/tmp/hr_customization",

    #  TODO: either make proper summary or delete this section at all
    'summary': "Short (1 phrase/line) summary of the module's purpose",

    #  TODO: make proper description
    'description': """
Long description of module's purpose
    """,

    #  TODO: either make proper author or delete this section at all
    'author': "My Company",
    #  TODO: either make proper website or delete this section at all
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    #  TODO: use version pattern: [Odoo_Version like 17.0].[module version like 0.1.9]
    #        in this specific case it would be 17.0.0.1.9
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
    #  TODO: if 'demo' section is empty and not planned - just delete it
    # only loaded in demonstration mode
    'demo': [
        # 'demo/demo.xml',
    ],
    'application': True,
 	'installable': True,
}
