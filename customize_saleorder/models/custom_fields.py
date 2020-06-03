# -*- coding: utf-8 -*-
from odoo import models, fields, api, _

class SaleOrder(models.Model):
    _inherit = 'sale.order'
    x_filenumber = fields.Char(string='File Number', required=True)


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'
    x_serialnumber = fields.Text(string='Serial Number', required=True)






