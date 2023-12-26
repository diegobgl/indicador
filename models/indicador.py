from odoo import models, fields, api
import requests

class Indicador(models.Model):
    _name = 'mi_modulo.indicador'
    _description = 'Indicador Económico'

    fecha = fields.Date('Fecha')
    valor = fields.Float('Valor')
    tipo_indicador  = fields.Selection([
        ('usd', 'USD'),
        ('eur', 'EUR'),
        # Add other currencies as needed
    ], string='tipo indicador ')


    #@api.model
    def actualizar_indicador(self):
        response = requests.get('https://mindicador.cl/api/dolar')
        data = response.json()
        for d in data['serie']:
            self.create({'fecha': d['fecha'][:10], 'valor': d['valor']})

    #@api.multi
    def consultar_indicador(self):
        for record in self:
            # Asegúrate de que el tipo de indicador y la fecha estén establecidos
            if not record.tipo_indicador or not record.fecha:
                raise ValueError('El tipo de indicador y la fecha deben estar especificados.')

            # Formatear la fecha para la consulta de la API
            fecha_formato_api = fields.Date.from_string(record.fecha).strftime('%d-%m-%Y')

            # Construir la URL para la consulta de la API
            url = 'https://www.mindicador.cl/api/{}/{}'.format(record.tipo_indicador, fecha_formato_api)

            # Realizar la solicitud a la API
            response = requests.get(url)
            if response.status_code != 200:
                # Puedes manejar diferentes códigos de estado de HTTP aquí, si es necesario
                raise ValueError('No se pudo obtener la información de la API o no existe información para la fecha dada.')

            # Parsear la respuesta JSON de la API
            data = response.json()
            valores = data.get('serie', [])

            # Asumimos que la serie contiene un solo valor para la fecha dada
            if valores:
                valor_indicador = valores[0].get('valor')
                # Actualizar el campo 'valor' con el valor del indicador económico
                record.valor = valor_indicador
            else:
                # Manejar la situación donde no hay datos para la fecha
                record.valor = None
                return {
                    'warning': {
                        'title': 'Sin datos',
                        'message': 'No se encontraron datos para la fecha dada.',
                    },
                }