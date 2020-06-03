# -*- coding: utf-8 -*-
from odoo.exceptions import ValidationError
from odoo import models, fields, api


class Picking(models.Model):
    _inherit = 'stock.picking'
    x_test = fields.Char(string="File Number", related='sale_id.x_filenumber')

