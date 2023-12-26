# Aquí puedes agregar tus controladores para las vistas web
from odoo import http

class MainController(http.Controller):
    @http.route('/mi_modulo/indicadores', auth='public')
    def list_indicadores(self, **kw):
        # Lógica para mostrar los indicadores
        return "Lista de Indicadores Económicos"
