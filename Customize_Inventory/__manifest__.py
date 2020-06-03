# -*- coding: utf-8 -*-
{
    'name': 'Custom Fields in sale Order Lines',
    'version': '12.0.1.0.0',
    'category': 'Extra Tools',
    'summary': 'Module for custom fields in sale order lines',
    'sequence': '101',
    'license': 'AGPL-3',
    'author': 'AB',
    'maintainer': 'AB',
    'website': 'ab.com',
    'depends': ['base', 'sale', 'stock', 'customize_saleorder'],
    'demo': [],
    'data': [
        
        'views/deliveryorder_inherit_view.xml',
        'views/view_related_serialnumber.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,

}