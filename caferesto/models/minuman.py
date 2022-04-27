from odoo import api, fields, models


class Minuman(models.Model):
    _name = 'caferesto.minuman'
    _description = 'Minuman'

    name = fields.Char(string='Menu')
    pilihan = fields.Selection(string='Pilihan', selection=[('ice', 'Ice'), ('hot', 'Hot'),])
    harga = fields.Integer(string='Harga')
    
