from odoo import fields, models,api,_
from datetime import date
from odoo.exceptions import ValidationError

class SaleOrder(models.Model):
    _inherit = "sale.order" #This will be the table name.
