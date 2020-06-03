# -*- coding: utf-8 -*-

from odoo import models, fields, api


class AccountInvoiceLine(models.Model):
    @api.model
    def get_serial_number(self):
        for rec in self:
            res = rec.env['sale.order'].search([('name', '=', rec.origin)])
            rec.so_reference = res

    so_reference = fields.Many2one('sale.order', compute='get_serial_number')  # adding reference of sale order
    _inherit = 'account.invoice.line'
    x_serialnumber = fields.Text(string="Serial Number", related='so_reference.order_line.x_serialnumber')
