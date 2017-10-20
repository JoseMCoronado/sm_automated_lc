# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Calculated Landed Costs From PO/Picking',
    'category': 'Purchase',
    'summary': 'Custom',
    'version': '1.0',
    'description': """
Automated landed costs on button click on stock.picking
        """,
    'depends': ['base','stock_landed_costs'],
    'data': [
        'data/ir_models.xml',
        'data/ir_model_access.xml',
        'data/ir_model_fields.xml',
        'data/ir_actions_server.xml',
        'data/ir_ui_views.xml',
    ],
    'installable': True,
    'application': False,
}
