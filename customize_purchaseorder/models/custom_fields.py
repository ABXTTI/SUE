# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from odoo.exceptions import UserError, RedirectWarning, ValidationError
from odoo.tools import float_is_zero



class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'
    
    x_filenumber = fields.Char(string='File Number', required=True, store=True)

    x_origin_ref = fields.Char(string='Origin Reference', store=True)

    

class PurchaseOrderLine(models.Model):
    _inherit = 'purchase.order.line'
    
    x_serialnumber = fields.Text(string='Serial Number', required=True, store=True)


