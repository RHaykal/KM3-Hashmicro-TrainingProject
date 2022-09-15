from email.policy import default
from odoo import api, models, fields

class RegistPoli(models.Model):
    _name = 'hospital.registrawatinap'
    _description = 'New Description'

    name = fields.Integer('No. Registrasi')
    patientName_id = fields.Many2one('hospital.pasien', string='Nama Pasien')
    roomNo_id = fields.Many2one('hospital.ruangrawatinap', string='Ruangan')
    doctorAssigned_id = fields.Many2one('hospital.dokter', string='Dokter in Control')
    registDate = fields.Date(string='Tgl Pendaftaran', default=fields.Datetime.now())
    state = fields.Selection([
        ('awaiting', 'Awaiting Payment'),
        ('verification', 'On Verification'),
        ('confirmed', 'Confirmed'),
    ], string='Status Pembayaran', default='awaiting', readonly=True)

    def action_verificating(self):
        self.write({'state': 'verification'})
    
    def action_confirmed(self):
        self.write({'state': 'confirmed'})

    def action_awaiting(self):
        self.write({'state': 'awaiting'})