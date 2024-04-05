from dash import html
from dash import dcc

CANDY_TYPES = [
    "chocolate",
    "fruity",
    "caramel",
    "peanutyalmondy",
    "nougat",
    "crispedricewafer",
    "hard",
    "bar",
    "pluribus",
]


def set_layout(app, df, vizs=[]):

    app.layout = html.Div(
        className="content",
        children=[
            html.Header(
                children=[
                    html.H1(app.title),
                ]
            ),
            html.Main(
                id="main",
                className="viz-container",
                children=[
                    html.Div(
                        id="viz1-graph",
                        style={"width": "100%"},
                        children=[
                            html.P(
                                className="storyline lead",
                                children=[
                                    "Le temps de l'halloween est parfait pour manger des bonbons. Mais quels bonbons sont les meilleurs? On veut savoir queles bonbon sont les plus apréciés des enfants, tout en respectant le portefeuille 💸 et le Dentiste 🦷"
                                ],
                            ),
                            dcc.Graph(
                                id="viz1-1",
                                className="graph",
                                figure=vizs[0].get_figure(df),
                            ),
                            html.Div(
                                id="type-menu-div",
                                style={"display": "flex", "justify-content": "center"},
                                children=[
                                    dcc.Checklist(
                                        id="type-menu",
                                        options=CANDY_TYPES,
                                        value=CANDY_TYPES,
                                        inline=True,
                                        labelStyle={"margin-right": "10px"},
                                    )
                                ],
                            ),
                        ],
                    )
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
