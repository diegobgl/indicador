{
    'name': 'Integración con Mindicador.cl',
    'version': '1.0',
    'summary': 'Consulta el valor del dólar y almacena consultas históricas',
    'sequence': 10,
    'description': "Integración con API de Mindicador.cl",
    'category': 'Extra Tools',
    'website': 'https://www.miwebsite.com',
    'depends': ['base', 'web'],
    'data': [
        'security/ir.model.access.csv',
        'views/indicador_view.xml',
       # 'views/templates.xml',
        #'data/cron.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}