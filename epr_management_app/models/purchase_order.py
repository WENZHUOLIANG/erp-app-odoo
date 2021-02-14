from odoo import api, fields, models

class PurchaseOrder(models.Model):
    _name = "wen.purchase.order.header"
    _description = "Purchase Order Header"

    shipping_address = fields.Char(string='Shipping Address')

    # Purchase Order Information(Header)
    po_number = fields.Char(string='PO Number')
    purchase_date = fields.Date(string="Purchase Date")
    delivery_date = fields.Date(string="Delivery Date")
    shipping_method = fields.Char(string="Shipping Method")
    shipping_terms = fields.Text(string='Note')
    buyer = fields.Many2one('wen.buyer', string="Buyer")
    # buyer = fields.Many2one('res.partner', string="Buyer")
    vendor = fields.Many2one('wen.vendor', string="Vendor")
    # buyer = fields.Many2one('res.partner', string="Buyer")

    state = fields.Selection([
        ('draft', 'Draft'),
        ('sent', 'Sent'),
        ('processing', 'Processing'),
        ('received', 'Received'),
        ('paid', 'Paid')],
        'State', default="draft")

    @api.model
    def is_allowed_transition(self, old_state, new_state):
        allowed = [('draft', 'sent'),
                   ('sent', 'processing'),
                   ('processing', 'received'),
                   ('received', 'paid')]
        return (old_state, new_state) in allowed

    @api.model
    def change_state(self, new_state):
        for purchase_order in self:
            if purchase_order.is_allowed_transition(purchase_order.state, new_state):
                purchase_order.state = new_state
            else:
                continue

    def make_sent(self):
        self.change_state('sent')

    def make_processing(self):
        self.change_state('processing')

    def make_received(self):
        self.change_state('received')

    def make_paid(self):
        self.change_state('paid')

    # Purchase Order Information(Detail)
    purchase_order_details = fields.One2many('wen.purchase.order.detail', 'order_id', string="Order Details")

    # Notes
    note = fields.Text(string='Note')

    # Count of Items
    count_item = fields.Integer(string='order item count', compute='_compute_count_item')

    # Total Price
    total_price = fields.Float(string='total price', compute='_compute_total_price')

    @api.depends('purchase_order_details')
    def _compute_count_item(self):
        for r in self:
            for o in r.purchase_order_details:
                print(o.price)
            r.count_item = len(r.purchase_order_details)

    @api.depends('purchase_order_details')
    def _compute_total_price(self):
        for r in self:
            for o in r.purchase_order_details:
                r.total_price += o.subtotal

    def name_get(self):
        result = []
        for record in self:
            rec_name = "%s (%s)" % (record.po_number, record.vendor.company_name)
            result.append((record.id, rec_name))
        return result


class PurchaseOrderDetails(models.Model):
    _name = "wen.purchase.order.detail"
    _description = "Purchase Order Detail"

    item_id = fields.Char(string='Item Id')
    quantity = fields.Integer(string='Quantity')
    price = fields.Float(string='Price', help='unit price of the product', digits="wen.product.price")
    product_id = fields.Many2one('wen.product', string="Product")
    order_id = fields.Many2one('wen.purchase.order.header',
                               ondelete='cascade', string="PO Header", required=True)
    subtotal = fields.Float(string='Subtotal', compute='_subtotal')

    # @api.onchange('price', 'quantity')
    @api.depends('price', 'quantity')
    def _subtotal(self):
        for r in self:
            r.subtotal = r.price * r.quantity

    _sql_constraints = [
        ('product_uniq', 'UNIQUE(id, product_id)', 'Product must be unique in each order'),
    ]
