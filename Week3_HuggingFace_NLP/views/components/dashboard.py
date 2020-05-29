import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc

from server import app


left_panel=html.Div(
    children=[
        # title
        html.Div([
            html.Span(
                children='Welcome to our demo!',
                style={'font-family': 'Inter-semibold', 'font-size': '28px'}
            ),
            html.Br(),
            html.Span(
                children='This is our demo for week 3 of Dataset Daily - NLP. Hopefully you find this useful and can find a use for the template in your own work.',
                style={'font-family': 'Inter-regular', 'font-size': '18px', 'word-wrap': 'break-word'}
            ),
        ],style={'width':'90%', 'margin-left': '5%'}),
        html.Div([
            html.Span(
                children="New to Dataset Daily? ",
                style={'color': 'grey', 'font-family': "Inter-reg"}
            ),
            html.Span(
                html.A("Sign Up", href="https://www.datasetdaily.com", target="__blank", style={'font-family': "Inter-reg", 'text-decoration': 'none', 'color': 'rgb(255, 115, 0)'}),
            )
        ],style={'margin-left': '5%', 'margin-top': '14px', 'font-size': '15px',}),
    ]
)

right_panel=html.Div(
    children=[
        html.Span(
            children='Dataset Daily NLP Demo Template',
            style={'font-family': 'Inter-semibold', 'font-size': '34px'}
        ),
        dcc.Textarea(
            id="input", 
            placeholder="Enter your text...",
            style={'margin-top': '14px'}
        ),
    ],style={'margin-left': '10%'},
)

