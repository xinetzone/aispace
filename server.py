try:
    from jupyter_dash import JupyterDash as Dash
except:
    from dash import Dash


NAME = __name__

META_TAGS = [
    {
        'name': 'description',
        'content': 'Using AI to develop anything interesting'
    },
    # A tag that tells the browser not to scale
    # desktop widths to fit mobile screens.
    # Sets the width of the viewport (browser)
    # to the width of the device, and the zoom level
    # (initial scale) to 1.
    #
    # Necessary for "true" mobile support.
    {
        'name': 'viewport',
        'content': 'width=device-width, initial-scale=1, shrink-to-fit=no'
    }
]


def create_app(name=NAME, title='Dash', **kwargs):
    kw = {
        'meta_tags': META_TAGS,
        'external_stylesheets': ['https://xinetzone.github.io/Font-Awesome/css/all.css',
                                 'https://xinetzone.github.io/w3css/4/w3.css',
                                 'https://xinetzone.github.io/xinet-css/tabs.css'],
        # 'external_scripts': ['https://www.google-analytics.com/analytics.js']
    }
    kwargs.update(kw)
    return Dash(name, title=title, **kwargs)


async def run_server(app, layout, host='127.0.0.1', port=10000, debug=True):
    # host='0.0.0.0'
    # app = create_app()
    app.layout = layout
    app.run_server('external', host=host, port=port, debug=debug)
