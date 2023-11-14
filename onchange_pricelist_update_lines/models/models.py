# -*- coding: utf-8 -*-

from odoo import models, api, fields, _


class SaleOrder(models.Model):
    _inherit = "sale.order"

    show_update_pricelist = fields.Boolean(string='Has Pricelist Changed',
                                           help="Technical Field, True if the pricelist was changed;\n"
                                                " this will then display a recomputation button")

    # @api.onchange('pricelist_id')
    # def update_order_lines(self):
    #     if self.order_line:
    #         order_line = []
    #         for line in self.order_line:
    #             order_line.append([0, 0, {
    #                 'product_id': line.product_id.id,
    #                 'product_uom_qty': line.product_uom_qty
    #             }])
    #         self.order_line = False
    #         self.order_line = order_line
    #         for line in self.order_line:
    #             line.product_id_change()

    @api.onchange('pricelist_id')
    def _onchange_pricelist_id(self):
        if self.order_line and self.pricelist_id and self._origin.pricelist_id and self._origin.pricelist_id != self.pricelist_id:
            self.show_update_pricelist = True
        else:
            self.show_update_pricelist = False

    def update_prices(self):
        self.ensure_one()
        lines_to_update = []
        for line in self.order_line.filtered(lambda line: not line.display_type):
            product = line.product_id.with_context(
                partner=self.partner_id,
                quantity=line.product_uom_qty,
                date=self.date_order,
                pricelist=self.pricelist_id.id,
                uom=line.product_uom.id
            )
            price_unit = self.env['account.tax']._fix_tax_included_price_company(
                line._get_display_price(product), line.product_id.taxes_id, line.tax_id, line.company_id)
            lines_to_update.append((1, line.id, {'price_unit': price_unit}))
        self.update({'order_line': lines_to_update})
        self.show_update_pricelist = False
        self.message_post(body=_(
            "Product prices have been recomputed according to pricelist <b>" + self.pricelist_id.display_name + "<b> "))
