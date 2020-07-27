# -*- coding: utf-8 -*-

from odoo import models, fields, api
import time

class AccountInvoiceLine(models.Model):
    _inherit = 'account.invoice.line'

    x_serialnumber = fields.Text(string="Serial Number")


class CurrencyRate(models.Model):
    _inherit = 'res.currency.rate'
   

    @api.depends('x_rate')
    def calrate(self):
    print ('api depends')
    for rec in self:
       rec.rate = 1 / rec.x_rate

    rate = fields.Float(digits=(12, 12), default=1.0, compute='calrate', help='The rate of the currency to the currency of rate 1')
    x_rate = fields.Float(digits=(12, 12), default=1.0, help='The rate of the currency to the currency of rate 1')
