import pandas as pd
from dash import html
from dash import dcc

CANDY_TYPES = [
    {'label': "chocolate", 'value': "chocolate"},
    {'label': "fruity", 'value': "fruity"},
    {'label': "caramel", 'value': "caramel"},
    {'label': "peanuty & almondy", 'value': "peanutyalmondy"},
    {'label': "nougat", 'value': "nougat"},
    {'label': "crisped rice wafer", 'value': "crispedricewafer"},
    {'label': "hard", 'value': "hard"},
    {'label': "bar", 'value': "bar"},
    {'label': "pluribus", 'value': "pluribus"},
]


def set_layout(app, df: pd.DataFrame, vizs: list = []):

    app.layout = html.Div(
        className="content",
        children=[
            html.Header(
                children=[
                    html.H1(app.title),
                ]
            ),
            html.Main(
                id="viz-container",
                children=[
                    html.Div(
                        id="viz1",
                        style={"width": "100%"},
                        children=[
                            html.P(
                                className="storyline lead",
                                children=[
                                    "Le temps de l'halloween est parfait pour manger des bonbons. Mais quels bonbons sont les meilleurs? On veut savoir queles bonbon sont les plus apréciés des enfants, tout en respectant le portefeuille 💸 et le Dentiste 🦷"
                                ],
                            ),
                            dcc.Graph(
                                id="viz1-graph",
                                className="graph",
                                figure=vizs[0].get_figure(df),
                            ),
                            html.Div(
                                id="candy-type-menu-div",
                                style={"display": "flex", "justify-content": "center"},
                                children=[
                                    dcc.Checklist(
                                        id="candy-type-menu",
                                        options=CANDY_TYPES,
                                        value=[r["value"] for r in CANDY_TYPES],
                                        inline=True,
                                        labelStyle={"margin-right": "10px"},
                                    )
                                ],
                            ),
                        ],
                    ),
                    html.Div(
                        id="viz2",
                        style={"width": "100%"},
                        children=[
                            dcc.Graph(
                                id="viz2-graph",
                                className="graph",
                                figure=vizs[0].get_figure(df),
                            ),
                            html.Div(
                                id="candy-choice-menu-div",
                                style={
                                    "display": "flex",
                                    "justify-content": "center",
                                    "flex-direction": "row",
                                    "width": "100%",
                                },
                                children=[
                                    dcc.Dropdown(
                                        style={"width": "20em"},
                                        id="candy-choice-menu",
                                        options=df["competitorname"].unique().tolist(),
                                    ),
                                    html.Div(style={"width": "5em"}),
                                    html.Div(
                                        style={"width": "30em"},
                                        children=[
                                            dcc.Slider(
                                                id="candy-proximity",
                                                value=1,
                                                min=1,
                                                step=1,
                                                max=9,
                                                marks={i: f"{i}+" for i in range(9)},
                                            )
                                        ],
                                    ),
                                ],
                            ),
                        ],
                    ),
                    html.Div(
                        id="viz3",
                        style={"width": "100%"},
                        children=[
                            dcc.Graph(
                                id="viz3-graph",
                                className="graph",
                                figure=vizs[1].get_figure(df),
                            ),
                        ],
                    ),
                    html.Div(
                        id="viz4",
                        style={"width": "100%"},
                        children=[
                            dcc.Graph(
                                id="viz4-graph",
                                className="graph",
                                figure=vizs[2].get_figure(df),
                            ),
                        ],
                    ),
                ],
            ),
            html.Footer(
                children=[
                    html.P(
                        children=[
                            "Données fournies par ",
                            html.A(
                                "five thirthy eight",
                                href="https://github.com/fivethirtyeight/data/tree/master/candy-power-ranking",
                            ),
                        ]
                    ),
                    html.P(
                        "Maxime Laroche - 1950276, Félix Blanchard - 2285987, Mehdi Belchiti - 2190903, Zakaria HANIRI - 2187461, Abdellatif KTAIB - 2212233, Juliette Arcouet - 1848701"
                    ),
                ]
            ),
        ],
    )
