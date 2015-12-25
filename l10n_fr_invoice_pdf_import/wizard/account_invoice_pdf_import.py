# -*- coding: utf-8 -*-
##############################################################################
#
#    L10n FR Invoice PDF import module for Odoo
#    Copyright (C) 2015 Akretion (http://www.akretion.com)
#    @author Alexis de Lattre <alexis.delattre@akretion.com>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from openerp import models, api


class AccountInvoicePdfImport(models.TransientModel):
    _inherit = 'account.invoice.pdf.import'

    @api.model
    def _select_partner(self, parsed_inv):
        if parsed_inv.get('siren'):
            siren = parsed_inv['siren'].replace(' ', '')
            if len(siren) == 9:
                partners = self.env['res.partner'].search([
                    ('supplier', '=', True),
                    ('is_company', '=', True),
                    ('siren', '=', siren),
                    ])
                if partners:
                    return partners[0]
        return super(AccountInvoicePdfImport, self)._select_partner(parsed_inv)
