from odoo import models, fields, api

class ResPartner(models.Model):
    _inherit = "res.partner"

    stn_razon_social = fields.Char(string="Razón Social", index=True)

    _rec_names_search = ['name', 'stn_razon_social']

    @api.depends('name', 'stn_razon_social')
    def _compute_display_name(self):
        for record in self:
            if record.stn_razon_social:
                record.display_name = f"{record.name} - {record.stn_razon_social}"
            else:
                record.display_name = record.name

    