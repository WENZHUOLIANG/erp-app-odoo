from odoo import api, fields, models

class Vendor(models.Model):
    _name = "wen.vendor";

    # buyer information
    company_name = fields.Char(string='Company Name')
    email_address = fields.Char(string='Email Address')
    address = fields.Char(string='Address')
    city = fields.Char(string='City')
    zipCode = fields.Char(string='Zip Code')
    country = fields.Char(string='Country')
    state = fields.Char(string='State')