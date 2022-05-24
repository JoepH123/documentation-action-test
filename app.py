import base64
import flask
import dash
import dash_bootstrap_components as dbc
from dash import html, Input, Output, State, callback_context, dcc
from src.apps import overview, teamdna, case_explorer, settings, insight_engine, lbp

external_scripts = ['https://code.jquery.com/jquery-3.2.1.slim.min.js',
                    'https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js',
                    'https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js']

external_stylesheets = [
    dbc.themes.BOOTSTRAP,
    "assets/customized.css",
    # "https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/css/materialize.min.css",
    "https://fonts.googleapis.com/css?family=Roboto&display=swap",
]

# Server definition
server = flask.Flask(__name__)
app = dash.Dash(__name__,
                external_stylesheets=external_stylesheets,
                external_scripts=external_scripts,
                server=server)

with open("assets/menu.png", "rb") as image_file:
    encoded_string_logo = base64.b64encode(image_file.read()).decode()
menu_img = "data:image/png;base64," + encoded_string_logo

with open("assets/KNVB.png", "rb") as image_file:
    encoded_string_logo = base64.b64encode(image_file.read()).decode()
KNVB_logo = "data:image/png;base64," + encoded_string_logo

with open("assets/JADS.png", "rb") as image_file:
    encoded_string_logo = base64.b64encode(image_file.read()).decode()
JADS_logo = "data:image/png;base64," + encoded_string_logo

title_nav = {
    "fontWeight": "bold",
    "fontSize": "24pt",
    "color": "white",
    "marginLeft": "5%",
    "marginRight": "2%",
    "width": "100%",
}

tabs = [("Overview", "overview"), ("Team DNA", "teamdna"), ("Insight Engine", "insight_engine"),
        ("Case Explorer", "case_explorer"), ("Line Breaking Passes", "lbp"), ("Settings", "settings")]

offcanvas = html.Div(
    [
        dbc.Button(id="open-offcanvas", outline=True, n_clicks=0, children=[html.Img(src=menu_img)], className="me-1"),
        dbc.Offcanvas(
            dbc.ListGroup(
                [
                    dbc.ListGroupItem(dbc.Button(name, id=f"{identifier}_button", outline=True), active=(i == 0),
                                      id=f"{identifier}_listgroup")
                    for i, (name, identifier) in enumerate(tabs)
                ]
            ),
            id="offcanvas",
            is_open=False,
        ),
    ],
    style={'width': '8%', 'display': 'inline-block'}
)
app.layout = html.Div(
    style={"height": "100%", 'width': '100%'},
    className="blue lighten-5",
    children=[
        dcc.Location(id='url', refresh=False, pathname=''),
        html.Div(
            style={"height": "90px", "margin": "0%", "padding": "10px", 'width': '100%', 'display': 'inline-block',
                   'backgroundColor': '#f36d2e'},
            className="card orange darken-4",
            children=[
                html.Img(style={"width": "50px", "marginRight": "10px", "float": "left"}, src=KNVB_logo),
                offcanvas,
                html.Div(children=[html.Label("KNVB Game Analyzer", style=title_nav, id='log')],
                         style={'width': '20%', 'display': 'inline-block', }),
                html.Div(children=[html.Img(style={"width": "100%", }, src=JADS_logo)],
                         style={'width': '13%', 'display': 'inline-block', "float": "right"}),
            ],
        ),
        html.Div(id="tab_content", style={"minHeight": "85vh"}),
    ],
)


@app.callback(
    Output("offcanvas", "is_open"),
    Input("open-offcanvas", "n_clicks"),
    [State("offcanvas", "is_open")],
)
def toggle_offcanvas(n1, is_open):
    if n1:
        return not is_open
    return is_open


# Change the url based on the navigation button that is pressed
@app.callback(Output('url', 'pathname'), [Input(f"{identifier}_button", "n_clicks") for _, identifier in tabs])
def change_url(*args):
    trigger = callback_context.triggered[0]
    button_pressed = trigger["prop_id"].split(".")[0]
    return f"/apps/{button_pressed[:-7]}"


# Navigation callback. Input is the url, output is the content of the page
@app.callback(
    [Output(f"{identifier}_listgroup", "active") for _, identifier in tabs] + [Output("tab_content", "children")],
    [Input('url', 'pathname')])
def func(url):
    button_pressed = url.split('/')[-1]
    buttons = [f"{identifier}" for _, identifier in tabs]
    result = [False for _ in range(len(buttons))]
    if len(button_pressed) == 0:
        button_pressed = 'overview'
    index_pressed = buttons.index(button_pressed)
    result[index_pressed] = True
    content = eval(f"{button_pressed}.layout")
    return result + [content]


if __name__ == '__main__':
    app.run_server(debug=True)
