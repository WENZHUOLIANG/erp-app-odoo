from odoo import api, fields, models

class Product(models.Model):
    _name = "wen.product";

    # product information
    product_id = fields.Char(string='Product Id')
    product_description = fields.Char(string='Product Description')

    def name_get(self):
        result = []
        for record in self:
            rec_name = "%s (%s)" % (record.product_description, record.product_id)
            result.append((record.id, rec_name))
        return result