# -*- coding: utf-8 -*-
{
    'name': "HỆ THỐNG QUẢN LÝ BÁN HÀNG",

    'summary': "NGUYỄN THẾ VĂN - 2022600297",

    'description': """
Hoc Lap Trinh Odoo - He quan tri doanh nghiep dien tu ERP
    """,

    'author': "Nguyen The Van",
    'website': "https://www.banhang.vn",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Hệ thống QLBH',
    'version': '0.1',
    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'data/demo.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

