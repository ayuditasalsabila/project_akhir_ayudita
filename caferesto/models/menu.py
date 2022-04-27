from odoo import api, fields, models


class Menu(models.Model):
    _name = 'caferesto.menu'
    _description = 'Menu Caferesto'

    name = fields.Char(string='Menu')
    harga = fields.Integer(string='Harga')
    
    
