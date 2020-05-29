# Dash app initialization
import dash

app = dash.Dash(
    __name__,
    meta_tags=[
        {
            'charset': 'utf-8',
        },
        {
            'name': 'viewport',
            'content': 'width=device-width, initial-scale=1, shrink-to-fit=no'
        }
    ]
)
server = app.server

app.config.suppress_callback_exceptions = True
app.title = 'NLP - Dataset Daily Sample App'

