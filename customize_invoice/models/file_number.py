# -*- coding: utf-8 -*-

from odoo import models, fields, api


class AccountInvoice(models.Model):

    @api.model
    def get_file_number(self):
        for rec in self:
            res = rec.env['sale.order'].search([('name', '=', rec.origin)])
            rec.so_reference = res

    _inherit = 'account.invoice'
    so_reference = fields.Many2one('sale.order', compute='get_file_number', readonly=False)
    x_filenumber1 = fields.Char(string="File Number", related='so_reference.x_filenumber')



