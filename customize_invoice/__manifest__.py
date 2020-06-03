# -*- coding: utf-8 -*-
{
    'name': 'Custom Related field in Invoice',
    'version': '12.0.1.0.0',
    'category': 'Extra Tools',
    'summary': 'Module for custom fields in Invoice',
    'sequence': '105',
    'license': 'AGPL-3',
    'author': 'AB',
    'maintainer': 'AB',
    'website': 'ab.com',
    'depends': ['base','customize_saleorder','account','account_accountant'],
    'demo': [],
    'data': [

        'views/file_and_serial_number.xml',
        'views/serial_number.xml'
    ],
    'installable': True,
    'application': True,
    'auto_install': False,

}