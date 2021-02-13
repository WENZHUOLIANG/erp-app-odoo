from odoo import api, fields, models

class PurchaseOrder(models.Model):
    _name = "wen.purchase.order.header"

    shipping_address = fields.Char(string='Shipping Address')

    # Purchase Order Information(Header)
    po_number = fields.Char(string='PO Number')
    purchase_date = fields.Date(string="Purchase Date")
    delivery_date = fields.Date(string="Delivery Date")
    shipping_method = fields.Char(string="Shipping Method")
    shipping_terms = fields.Text(string='Note')
    buyer = fields.Many2one('wen.buyer', string="Buyer")
    vendor = fields.Many2one('wen.vendor', string="Vendor")

    # Purchase Order Information(Detail)
    purchase_order_details = fields.One2many('wen.purchase.order.detail', 'order_id', string="Order Details")

    # Notes
    note = fields.Text(string='Note')

class PurchaseOrderDetails(models.Model):
    _name = "wen.purchase.order.detail"

    item_id = fields.Char(string='Item Id')
    quantity = fields.Char(string='Quantity')
    price = fields.Char(string='Price')
    product_id = fields.Many2one('wen.product', string="Product")
    order_id = fields.Many2one('wen.purchase.order.header',
        ondelete='cascade', string="PO Header", required=True)