{
    'name': "Animated Snippets",
    'version': '16.0.1.0.0',
    'description': """""",
    'depends': ['base', 'website', 'web_editor'],
    'data': [
        'views/snippets/snippets.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            '/animated_snippet/static/src/css/animated_circle.css',
        ]},
    'installable': True,
    'auto_install': False,
    'application': False,
}