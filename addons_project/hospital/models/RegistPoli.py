from email.policy import default
from xml.dom import ValidationErr
from odoo import api, models, fields
from odoo.exceptions import ValidationError

class RegistPoli(models.Model):
    _name = 'hospital.registpoli'
    _description = 'New Description'

    name = fields.Integer('No. Registrasi')
    patientName_id = fields.Many2one('hospital.pasien', string='Nama Pasien')
    poliName_id = fields.Many2one('hospital.poli', string='Mendaftar ke Poli')
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

    def unlink(self):
        if self.filtered(lambda line: line.state != 'awaiting'):
            raise ValidationError("Tidak dapat menghapus record jika status bukan Awaiting Payment")
        return super(RegistPoli, self).unlink()