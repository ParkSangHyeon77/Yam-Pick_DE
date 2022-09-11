from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

app = Dash(__name__)

# Colors
bgcolor = "#f3f3f1"  # mapbox light map land color
bar_bgcolor = "#b0bec5"  # material blue-gray 200

# Figure template
row_heights = [150, 500, 300]
template = {"layout": {"paper_bgcolor": bgcolor, "plot_bgcolor": bgcolor}}

def blank_fig(height):
    """
    Build blank figure with the requested height
    """
    return {
        "data": [
            'hi',
        ],
        "layout": {
            "height": height,
            "template": template,
            "xaxis": {"visible": False},
            "yaxis": {"visible": False},
        },
    }

app.layout = html.Div(
    children=[
        html.Div(
            children=[
                html.H1(
                    [
                        "Yam-Pick",
                        html.A(
                            html.Img(
                                src="my_img/logo.png",
                                style={"float": "right", "height": "50px"},
                            ),
                        ),
                    ],
                    style={"text-align": "left"},
                ),
            ]
        ),
        html.Div(
            children=[
                html.Div(
                    children=[
                        html.H4(
                            [
                                "Daily Calorie"
                            ],
                            className="container_title"
                        ),
                        dcc.Graph(
                            id="indicator-graph",
                            figure={
                                "data": [
                                    {
                                        "type": "indicator",
                                        "value": 칼로리 데이터,
                                        "number": {"font": {"color": "#263238"}},
                                    }
                                ],
                                "layout": {
                                    "template": template,
                                    "height": 150,
                                    "margin": {"l": 10, "r": 10, "t": 10, "b": 10},
                                },
                            },
                            config={"displayModeBar": False},
                            className="svg-container",
                        )
                    ]
                ),
            ],
            className="six columns pretty_container",
            id="indicator-div",
        ),
    ]
)



if __name__ == '__main__':
    app.run_server(debug=True)