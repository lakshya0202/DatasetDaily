import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import json 
import requests
import plotly.graph_objects as go
from dash.dependencies import Input, Output


app = dash.Dash(__name__, meta_tags=[{"name": "viewport", "content": "width=device-width, initial-scale=1"}])
app.title = 'Economic History of the US'

server = app.server

df = pd.read_excel("data/economics.xlsx")

fig = go.Figure()
fig.update_layout(xaxis_showgrid=False, yaxis_showgrid=False, xaxis={'title': 'Date','fixedrange':True}, yaxis={'title': 'Value','fixedrange':True}, plot_bgcolor='rgb(255,255,255)', margin={'t': 15, 'b': 9},width=900,height=500)

app.layout = html.Div(
    [
        html.Div([
            html.Div([
                        html.Div(
                            [
                                html.H3(
                                    "United States Economic History",
                                    className="title",
                                ),
                                html.Span(
                                    "Look back on decades of economic history."
                                ),
                                html.Br(),
                                html.Br(),
                                html.A(html.Button("Built as a demo for week 2 of Dataset Daily - Economics."), href="https://www.datasetdaily.com", target="_blank"),
                            ]
                        )
                    ],
                    className="app__header",
                ),
                html.Div(
                    [
                        html.Div(
                            [
                                html.Div(
                                    [
                                        dcc.Dropdown(
                                            id="economics_dropdown",
                                            multi=False,
                                            value='industrial_production_index',
                                            options=[{"label": i, "value": i} for i in list(df.columns.values)],
                                            placeholder='Pick an economic indicator...',
                                        )
                                    ],
                                    className="app__dropdown",
                                ),
                                html.Br(),
                                html.Span("Tip: Drag to zoom, double click to reset."),
                                dcc.Loading(id = "loading-icon-ta", children=[html.Div(dcc.Graph(id="economics_graph",
                                    figure=fig, 
                                    config={'displayModeBar': False, 'scrollZoom': False}))], type="default"),
                                html.Br(),
                                html.Br(),
                                html.Span("March release for "),
                                html.Span(
                                    id='metric_name',
                                    children='N/A - pick a metric above.'
                                ),
                                html.Span(
                                    id='metric_value',
                                    children=''
                                ),
                                html.Br(),
                            ],
                            className="two-thirds column",
                        ),
                    ],
                    className="container card app__content bg-white",
                    ),
            ],
            className="app__container",
        ),
    ]
)

################ ECONOMICS CHART ################
@app.callback(
    Output("economics_graph", "figure"),
    [Input("economics_dropdown", "value")],
)
def output_chart(metric):
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df['observation_date'], y=df[metric],name='',showlegend=False))
    fig.update_layout(
        xaxis_showgrid=False, 
        yaxis_showgrid=False, 
        xaxis={'title': 'Date'}, 
        yaxis={'title': 'Value'}, 
        plot_bgcolor='rgb(255,255,255)', 
        margin={'t': 15, 'b': 9},
        width=900,
        height=500
    )
    return (
        fig
    )

################ Latest Numbers ################
@app.callback(
    [Output("metric_name", "children"),
     Output("metric_value", "children"),
    ],
    [Input("economics_dropdown", "value")],
)
def output_values(metric):
    return(
        metric + ": ",
        f'{df[metric].iloc[-2]:,}'
    )

if __name__ == '__main__':
    app.run_server(host='0.0.0.0', debug=False)