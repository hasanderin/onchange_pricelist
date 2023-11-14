# -*- coding: utf-8 -*-
from odoo import http

# class OnchangePricelistUpdateLines(http.Controller):
#     @http.route('/onchange_pricelist_update_lines/onchange_pricelist_update_lines/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/onchange_pricelist_update_lines/onchange_pricelist_update_lines/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('onchange_pricelist_update_lines.listing', {
#             'root': '/onchange_pricelist_update_lines/onchange_pricelist_update_lines',
#             'objects': http.request.env['onchange_pricelist_update_lines.onchange_pricelist_update_lines'].search([]),
#         })

#     @http.route('/onchange_pricelist_update_lines/onchange_pricelist_update_lines/objects/<model("onchange_pricelist_update_lines.onchange_pricelist_update_lines"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('onchange_pricelist_update_lines.object', {
#             'object': obj
#         })