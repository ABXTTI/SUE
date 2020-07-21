# -*- coding: utf-8 -*-

from odoo import models, fields, api


class AccountInvoiceLine(models.Model):
    _inherit = 'account.invoice.line'

    x_serialnumber = fields.Text(string="Serial Number")


class CurrencyRate(models.Model):
    _inherit = 'res.currency.rate'
    rate = fields.Float(digits=(12, 6), compute='calrate', readonly=False)
    x_rate = fields.Float(digits=(12, 6), default=1.0, help='The rate of the currency to the currency of rate 1')

    @api.multi
    def calrate(self):
        for rec in self:
            rec.rate = 1 / rec.x_rate
            return rec.rate
