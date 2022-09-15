from odoo import api, fields, models

class Poli(models.Model):
    _name = 'hospital.poli'
    _description = 'New Description'

    name = fields.Char('Nama Poli')
    officer_ids = fields.One2many('hospital.dokter', 'postAssigned_id', string='Dokter yang bertugas')
    jml_dokter = fields.Char(compute='_compute_jml_dokter', string='Jumlah Dokter pada Poli')

    @api.depends('officer_ids')
    def _compute_jml_dokter(self):
        for record in self:
            a = self.env['hospital.dokter'].search([('postAssigned_id', '=', record.id)]).mapped('name')
            b = len(a)
            record.jml_dokter = b
            record.listDokter = a

    listDokter = fields.Char('Dokter Poli')

