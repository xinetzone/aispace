try:
    from jupyter_dash import JupyterDash as Dash
except:
    from dash import Dash


def create_app():
    external_stylesheets = [
        'https://xinetzone.github.io/Font-Awesome/css/all.css']
    app = Dash(__name__, external_stylesheets=external_stylesheets)
    return app


async def run_server(app, layout, host='127.0.0.1', port=10000, debug=True):
    # host='0.0.0.0'
    # app = create_app()
    app.layout = layout
    app.run_server('external', host=host, port=port, debug=debug)
