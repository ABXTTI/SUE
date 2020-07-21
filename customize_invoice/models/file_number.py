# -*- coding: utf-8 -*-

from odoo import models, fields, api


class AccountInvoice(models.Model):
    _inherit = 'account.invoice'
    
    x_filenumber1 = fields.Char(string="File Number")



