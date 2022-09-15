from odoo import api, fields, models

class Dokter(models.Model):
    _name = 'hospital.dokter'
    _description = 'New Description'

    dokterNo = fields.Integer(string='No.', required=True)
    name = fields.Char(string='Nama', required=True)
    age = fields.Integer(string='Usia')
    address = fields.Char(string='Alamat')
    scheduleDay = fields.Char('Hari Praktek')
    scheduleHour = fields.Char('Jam Praktek')
    postAssigned_id = fields.Many2one(comodel_name='hospital.poli', string='Poli')