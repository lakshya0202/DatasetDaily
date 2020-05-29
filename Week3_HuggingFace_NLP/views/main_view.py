import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc

from server import app
from views.components import dashboard

# uncomment if using the Keras implementation instead of Vader... Vader is much simpler :) 
'''
from keras.preprocessing.text import Tokenizer, tokenizer_from_json
from keras.preprocessing.sequence import pad_sequences
import pickle 
from keras.models import load_model
from keras.layers import RNN, GRU, LSTM, Dense, Input, Embedding, Dropout, Activation, concatenate
from keras.layers import Bidirectional, GlobalAveragePooling1D, GlobalMaxPooling1D
from keras.models import Model
from keras.callbacks import EarlyStopping, ModelCheckpoint
from keras import initializers, regularizers, constraints, optimizers, layers
'''
import numpy as np
import json 

# Simpler use for deployed sample, saving on compute 
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
analyzer = SentimentIntensityAnalyzer()


##### APPROACH USING PRE-TRAINED KERAS MODEL WITH 6 CATEGORIES #####
'''
# loading model + weights 
model = load_model('model.h5')
# loading tokenizer 
with open('tokenizer.json') as f:
    data = json.load(f)
    tokenizer = tokenizer_from_json(data)

max_features = 100000
max_len = 300
embed_size = 300
'''

layout = html.Div(
    [
        html.Div
        (
            [
                html.Div(
                    children=[
                        html.Div([
                            dashboard.left_panel
                        ]),
                    ],style={'margin-top': '50px'}
                ),
            ], style={'width': '30%', 'height' : '100vh', 'background-color': '#FFFFFF', 'overflow': 'scroll', 'display': 'inline-block', 'vertical-align': 'top', 'margin-left': '0%'},
        ),
        
        ##### Main section #####
        html.Div
        (
            [
                html.Div(
                    children=[
                        html.Div([
                            dashboard.right_panel,
                            html.Br(),
                            html.Span(
                                id='positivity_text',
                                children="Positivity Score: ",
                                style={'font-family': 'Inter-semibold', 'font-size': '25px', 'margin-left': '10%'}
                            ),
                            html.Span(
                                id='positivity_result',
                                children=None,
                                style={'font-family': 'Inter-regular', 'font-size': '25px'}
                            ),        
                            html.Br(),
                            html.Span(
                                id='negativity_text',
                                children="Negativity Score: ",
                                style={'font-family': 'Inter-semibold', 'font-size': '25px', 'margin-left': '10%'}

                            ),
                            html.Span(
                                id='negativity_result',
                                children=None,
                                style={'font-family': 'Inter-regular', 'font-size': '25px'}

                            ),                        

                        ])
                    ],style={'margin-top': '50px'}
                ),
            ], style={'font-size': '15px', 'width': '70%', 'height' : '100vh', 'overflow': 'scroll', 'display': 'inline-block', 'margin-bottom': '0px', 'vertical-align': 'top', 'background-color': '#F0F0F0', 'margin-left': '0%'},

        ),
    ],style={'font-size': '0px'}
)

@app.callback(
    [Output('positivity_result', 'children'), 
    Output('negativity_result', 'children'),],
    [Input('input', 'value'),
    ],
)
def tokenizer(text):
    
    #if n_clicks > 0:
        
    #super simple use of Vader for raw sentiment/polarity 
    score = analyzer.polarity_scores(text)
    print(score)
    return (
        score['pos'],
        score['neg'],
    )

    '''
    # This is inefficient and tokenizer should be loaded at top with model.
    # For some reason does not work when loaded at top, needs fixed... 
    with open('tokenizer.json') as f:
        data = json.load(f)
        tokenizer = tokenizer_from_json(data)
    tokenized_text = tokenizer.texts_to_sequences(text)
    padded_text = pad_sequences(tokenized_text, max_len)
    model = load_model('model.h5')
    test_values = model.predict([padded_text])  
    '''