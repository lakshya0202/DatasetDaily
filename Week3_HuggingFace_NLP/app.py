# index page
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from server import app, server
from views import main_view


app.layout = html.Div(
    [
        html.Div([
            html.Div(
                html.Div(id='page-content', className='content'),
            ),
        ]),
        dcc.Location(id='url', refresh=False),
    ]
)

@app.callback(
    Output('page-content', 'children'), 
    [Input('url', 'pathname'),])
def display_page(pathname):
    if pathname == '/':
        return main_view.layout
    else:
        return main_view.layout

if __name__ == '__main__':
    app.run_server(host='0.0.0.0', debug=False)
