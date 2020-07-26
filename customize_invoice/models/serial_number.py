# -*- coding: utf-8 -*-

from odoo import models, fields, api
import time

class AccountInvoiceLine(models.Model):
    _inherit = 'account.invoice.line'

    x_serialnumber = fields.Text(string="Serial Number")


class CurrencyRate(models.Model):
    _inherit = 'res.currency.rate'
    rate = fields.Float(digits=(12, 6), default=1.0, help='The rate of the currency to the currency of rate 1')

    x_rate = fields.Float(digits=(12, 6), default=1.0, help='The rate of the currency to the currency of rate 1')


    # @api.multi
    # @api.depends('rate','x_rate')
    # def calcrate(self):
    #     print ('api depends')
    #     for r in self:
    #         r.rate = 1 / r.x_rate
    @api.multi
    def write(self, vals):
        res=super(CurrencyRate, self).write(vals)
        self.rate=1/self.x_rate
        return res



