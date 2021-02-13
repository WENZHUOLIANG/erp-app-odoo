from odoo import api, fields, models

class Product(models.Model):
    _name = "wen.product";

    # product information
    product_id = fields.Char(string='Product Id')
    product_description = fields.Char(string='Product Description')