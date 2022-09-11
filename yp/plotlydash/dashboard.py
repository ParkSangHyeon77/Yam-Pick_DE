# # -*- coding: utf-8 -*-

# import dash
# import dash_core_components as dcc
# import dash_html_components as html
# from dash.dependencies import Input, Output
# from yp.models import tb_food_img

# # Colors
# bgcolor = "#f3f3f1"  # mapbox light map land color
# bar_bgcolor = "#b0bec5"  # material blue-gray 200

# # Figure template
# row_heights = [150, 500, 300]
# template = {"layout": {"paper_bgcolor": bgcolor, "plot_bgcolor": bgcolor}}

# def blank_fig(height):
#     """
#     Build blank figure with the requested height
#     """
#     return {
#         "data": [
#             'hi',
#         ],
#         "layout": {
#             "height": height,
#             "template": template,
#             "xaxis": {"visible": False},
#             "yaxis": {"visible": False},
#         },
#     }

# # Build Dash layout
# def create_dashboard(server):
#     dash_app = dash.Dash(
#         server=server,
#         url_base_pathname='/dashbord/',
#         assets_folder='plotlydash/assets'
#         )

#     food_being = tb_food_img.query.filter_by(food_name="된장찌개").first()
#     food_energy = food_being['energy']

#     dash_app.layout = html.Div(
#         children=[
#             html.Div(
#                 children=[
#                     html.H1(
#                         [
#                             "Yam-Pick",
#                             html.A(
#                                 html.Img(
#                                     src="static/img/logo.png",
#                                     style={"float": "right", "height": "50px"},
#                                 ),
#                             ),
#                         ],
#                         style={"text-align": "left"},
#                     ),
#                 ]
#             ),
#             html.Div(
#                 children=[
#                     html.Div(
#                         children=[
#                             html.H4(
#                                 [
#                                     "Daily Calorie"
#                                 ],
#                                 className="container_title"
#                             ),
#                             dcc.Graph(
#                                 id="indicator-graph",
#                                 figure={
#                                     "data": [
#                                         {
#                                             "type": "indicator",
#                                             "value": food_energy,
#                                             "number": {"font": {"color": "#263238"}},
#                                         }
#                                     ],
#                                     "layout": {
#                                         "template": template,
#                                         "height": 150,
#                                         "margin": {"l": 10, "r": 10, "t": 10, "b": 10},
#                                     },
#                                 },
#                                 config={"displayModeBar": False},
#                                 className="svg-container",
#                             )
#                         ]
#                     ),
#                 ],
#                 className="six columns pretty_container",
#                 id="indicator-div",
#             ),
#         ]
#     )

#     init_callbacks(dash_app)

#     return dash_app.server


# def init_callbacks(dash_app):
#     @dash_app.callback(
#         Output(component_id='my-output', component_property='children'),
#         Input(component_id='my-input', component_property='value')
#     )
#     def update_graph(rows):
#         pass
