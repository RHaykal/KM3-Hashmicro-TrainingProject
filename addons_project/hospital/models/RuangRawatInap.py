from odoo import api, fields, models

class RuangRawatInap(models.Model):
    _name = 'hospital.ruangrawatinap'
    _description = 'New Description'

    name = fields.Char('Nomor Ruangan')
    roomClass = fields.Selection([
        ('3', '3'),
        ('2', '2'),
        ('1', '1'),
        ('VIP', 'VIP'),
    ], string='Kelas')
    roomFloor = fields.Integer('Lantai Ruangan')
