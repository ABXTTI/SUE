# -*- coding: utf-8 -*-
from odoo import models, fields


class StockMove(models.Model):
    _inherit = 'stock.move'
    x_test2 = fields.Text(string="Serial Number", related='picking_id.sale_id.order_line.x_serialnumber')

    # x_filenumber = fields.Text("sale.order.x_filenumber", related='sale_.x_filenumber', string='File Number')
