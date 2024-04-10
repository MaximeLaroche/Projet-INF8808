import pandas as pd
from dash import html
from dash import dcc
import viz4.viz4 as viz4

CANDY_TYPES = [
    {"label": "chocolate", "value": "chocolate"},
    {"label": "fruity", "value": "fruity"},
    {"label": "caramel", "value": "caramel"},
    {"label": "peanuty & almondy", "value": "peanutyalmondy"},
    {"label": "nougat", "value": "nougat"},
    {"label": "crisped rice wafer", "value": "crispedricewafer"},
    {"label": "hard", "value": "hard"},
    {"label": "bar", "value": "bar"},
    {"label": "pluribus", "value": "pluribus"},
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
                            html.H3(
                                children="Appréciation générale des bonbons en fonction du prix et du taux de sucre"
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
                        style={"width": "100%", "padding-top": "3cm"},
                        children=[
                            html.P(
                                className="storyline lead",
                                children=[
                                    "Vous avez choisi d'acheter les bonbon les plus apprécié par la majorité des enfant, mais un enfant vous demande un bonbon en particulier que vous n'avez pas?. Le graphique suivant présente le taux d'appréciation des bonbons ayant le plus d'attribut commun avec le bonbon demandé par l'enfant. Ça pourrait sauver votre Halloween! 🎃 Simplement sélectioné le bonbon demandé et spécifier combien d'ingrédient en commun les bonbon doivent avoir pour s'afficher"
                                ],
                            ),
                            html.H3(
                                children="Meilleurs alternatives de substitution de bonbon"
                            ),
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
                        style={"width": "100%", "padding-top": "3cm"},
                        children=[
                            html.P(
                                className="storyline lead",
                                children=[
                                    "Durant toute soirée d'halloween, il y a le fameux débat pour déterminer quels sont les meilleurs ingrédients de bonbon. Certain jurent par le chocolat 🍫, d'autre par le caramel. Ici, vous trouverez la vérité une fois pour toute! L'appréciation général des bonbons est affiché dans le graphique suivant et les couleurs représente si un bonbon a une certaine caractéristique. Vous pourrez aussi voir si le chocolat est vraiment plus sucré que les fruits!"
                                ],
                            ),
                            html.H3(
                                children="Appréciation générale des bonbon en fonction du taux de sucre, du prix et identifier par leur ingrédients"
                            ),
                            dcc.Graph(
                                id="viz3-graph",
                                className="graph",
                                figure=vizs[1].get_figure(df),
                            ),
                        ],
                    ),
                    html.Div(
                        id="viz4_1",
                        style={"width": "100%", "padding-top": "3cm"},
                        children=[
                            html.P(
                                className="storyline lead",
                                children=[
                                    "Avec la quantité de bonbon dans le graphique précédent, il peu être difficile de voir les tendances. C'est pourquoi nous avons regroupé les bonbons en fonction de leur ingrédients. Vous pourrez voir les tendances plus facilement et peut-être même découvrir des combinaisons de bonbon que vous n'auriez jamais pensé essayer!"
                                ],
                            ),
                            html.H3(
                                children="Distribution de l'appréciation des bonbons en fonction de leur ingrédients"
                            ),
                            html.Div(
                                className="graph viz4",
                                children=[
                                    html.Div(
                                        style={"max-width": "25%"},
                                        children=[dcc.Graph(figure=fig)],
                                    )
                                    for fig in viz4.aliments
                                ],
                            ),
                        ],
                    ),
                    html.Div(
                        id="viz4_2",
                        style={"width": "100%", "padding-top": "3cm"},
                        children=[
                            html.P(
                                className="storyline lead",
                                children=[
                                    "Toutefois, la plutpart des bonbons comportent plus d'un ingrédient. Parfois, deux bonne chose ensemble peuvent ne pas être bon du tout et même, deux ingrédient très moyens ensemble peuvent être très appréciés. Nous avons alors pris la liberté de tracer les même courbes, mais cette fois-ci en fonction de la combinaison de deux ingrédients. Vous pourrez voir les tendances plus facilement et peut-être même découvrir des combinaisons de bonbon que vous n'auriez jamais pensé essayer!"
                                ],
                            ),
                            html.H3(
                                children="Distribution de l'appréciation des bonbons en fonction de la présence d'une combinaison d'ingrédients"
                            ),
                            html.Div(
                                className="graph viz4",
                                children=[
                                    html.Div(
                                        style={"max-width": "25%"},
                                        children=[dcc.Graph(figure=fig)],
                                    )
                                    for fig in viz4.combo_aliments
                                ],
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
