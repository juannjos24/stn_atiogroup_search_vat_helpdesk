from odoo import models, fields, api

class ResPartner(models.Model):
    _inherit = "res.partner"

    stn_razon_social = fields.Char(string="Razón Social", index=True)

    @api.depends('name', 'stn_razon_social')
    def _compute_display_name(self):
        for record in self:
            name = record.name or ""
            if record.stn_razon_social:
                record.display_name = f"{name} | {record.stn_razon_social}"
            else:
                record.display_name = name

    @api.model
    def _name_search(self, name, args=None, operator='like', limit=10, order=None):
        args = args or []
        
        if name:
            # Si el usuario escribe '415', Odoo buscará '415%' en la base de datos
            # Usamos '=like' para que el % que añadimos sea interpretado correctamente
            return self._search([('stn_razon_social', '=like', name + '%')] + args, limit=limit, order=order)
        
        return super()._name_search(name, args=args, operator=operator, limit=limit, order=order)