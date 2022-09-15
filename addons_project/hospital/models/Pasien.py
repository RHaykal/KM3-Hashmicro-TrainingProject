from email.policy import default
from odoo import api, fields, models

class Pasien(models.Model):
    _name = 'hospital.pasien'
    _description = 'New Description'

    pasienNo = fields.Integer(string='No', required=True)
    name = fields.Char(string='Nama Pasien', required=True)
    age = fields.Integer(string='Usia')
    dob = fields.Date(string='Tanggal Lahir')
    address = fields.Char(string='Alamat')
    have_asuransi = fields.Boolean(string='Asuransi', required=True, default=False)
    #TODO buat attribut conditioning untuk field attr model id_asuransi(if have_asuransi = True, id_asuransi = visible/editable)
    id_asuransi = fields.Char(string='No. Asuransi')