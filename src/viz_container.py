import pandas as pd
from dash import html
from dash import dcc
from itertools import chain
import dash_bootstrap_components as dbc

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
    viz12 = vizs[0].get_figure(df)
    viz3 = vizs[1].get_figure(df)
    viz4_1, viz4_2 = vizs[2].get_figures(df)

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
                                    "Le temps de l'Halloween est parfait pour manger des bonbons. Mais quels bonbons sont les meilleurs ? On veut connaître les bonbons les plus appréciés des enfants, tout en respectant le portefeuille des habitants du quartier 💸 et éviter si possible des bonbons trop sucrés 🦷."
                                ],
                            ),
                            html.H3(
                                children="Appréciation générale des bonbons en fonction du prix et du taux de sucre"
                            ),
                            dcc.Graph(
                                id="viz1-graph",
                                className="graph",
                                figure=viz12,
                            ),
                            html.Div(
                                id="candy-type-menu-div",
                                style={"display": "flex", "justify-content": "center"},
                                children=[
                                    dbc.ButtonGroup(
                                        id="candy-type-menu",
                                        children=list(
                                            chain(
                                                dbc.Checkbox(
                                                    id=f'candy-type-{r["value"]}',
                                                    value=False,
                                                    label=r["label"],
                                                    input_class_name=["btn-check"],
                                                    label_class_name=[
                                                        "btn",
                                                        "btn-outline-primary",
                                                    ],
                                                    style={"padding": "0.1rem"},
                                                )
                                                for r in CANDY_TYPES
                                            )
                                        ),
                                    )
                                ],
                            ),
                            html.P(
                                className="storyline lead",
                                children=[
                                    "Le graphique ci-dessus, possède un menu interactif (en bas) qui vous permet de sélectionner certains ingrédients désirés et les bonbons comprenant ces ingrédients apparaîtront. Vous pouvez aussi cliquer sur la légende des couleurs pour ne voir apparaitre que la catégorie que vous souhaitez."
                                ],
                            ),
                        ],
                    ),
                    html.Div(
                        id="viz2",
                        style={"width": "100%"},
                        children=[
                            html.H3(
                                children="Meilleures alternatives de substitution de bonbon"
                            ),
                            dcc.Graph(
                                id="viz2-graph",
                                className="graph",
                                figure=viz12,
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
                                        placeholder="Choisissez un bonbon...",
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
                                                tooltip={
                                                    "style": {"width": "10rem"},
                                                    "template": " au moins {value} similarités avec le bonbon choisi ",
                                                },
                                            )
                                        ],
                                    ),
                                ],
                            ),
                            html.P(
                                className="storyline lead",
                                children=[
                                    "Imaginons qu’un enfant vous demande un bonbon en particulier que vous n'avez pas. Le graphique ci-haut présente le taux d'appréciation des bonbons ayant le plus d'attributs communs avec le bonbon demandé par l'enfant. Ça pourrait sauver votre Halloween ! 🎃 Simplement, écrivez le bonbon demandé dans la barre de recherche et spécifiez combien d'ingrédients en commun les bonbons proposés doivent avoir avec celui recherché (un plus grand nombre sera gage d’une plus grande similarité). Les substituts vont ensuite s'afficher !"
                                ],
                            ),
                        ],
                    ),
                    html.Div(
                        id="viz3",
                        style={"width": "100%"},
                        children=[
                            html.H3(
                                children="Appréciation générale des bonbons en fonction du taux de sucre, du prix et identifier par leurs ingrédients"
                            ),
                            dcc.Graph(
                                id="viz3-graph",
                                className="graph",
                                figure=viz3,
                            ),
                            html.P(
                                className="storyline lead",
                                children=[
                                    "Durant toute soirée d'Halloween, il y a le fameux débat pour déterminer quels sont les meilleurs bonbons. Certains jurent uniquement par les barres de chocolat 🍫, d’autres par les bonbons fruités. Ici, vous trouverez la vérité une fois pour toutes ! L'appréciation générale des bonbons est affichée dans le graphique qui précède et les couleurs représentent si un bonbon a une certaine caractéristique. En analysant les données, il y a des clusters de bonbons qui ressortent : •	Les barres de chocolats (elles auront généralement des noix du caramel, etc.) •	Les paquets de bonbons au chocolat (type Smarties, Reese's,  etc.) •	Les paquets de bonbons aux fruits •	Les bonbons vendus à l'unité aux fruits"
                                ],
                            ),
                        ],
                    ),
                    html.Div(
                        id="viz4_1",
                        style={"width": "100%"},
                        children=[
                            html.H3(
                                children="Distribution de l'appréciation des bonbons en fonction de leurs ingrédients"
                            ),
                            dcc.Graph(
                                id="viz4_2-graph", className="graph", figure=viz4_1
                            ),
                            html.P(
                                className="storyline lead",
                                children=[
                                    "Avec la quantité de bonbons dans le graphique précédent, il peut être difficile de voir les tendances. C'est pourquoi nous avons regroupé les bonbons en fonction de leurs ingrédients. Le graphique ci-haut vous permet de voir les tendances plus facilement et peut-être même découvrir des combinaisons de bonbon que vous n'auriez jamais pensé essayer !"
                                ],
                            ),
                        ],
                    ),
                    html.Div(
                        id="viz4_2",
                        style={"width": "100%"},
                        children=[
                            html.H3(
                                children="Distribution de l'appréciation des bonbons en fonction de la présence d'une combinaison d'ingrédients"
                            ),
                            dcc.Graph(
                                id="viz4_1-graph", className="graph", figure=viz4_2
                            ),
                            html.P(
                                className="storyline lead",
                                children=[
                                    "Toutefois, la plupart des bonbons comportent plus d'un ingrédient. Parfois, deux bons ingrédients combinés ne sont pas très appréciés et inversement. Nous avons alors pris la liberté de tracer les mêmes courbes, mais cette fois-ci,  en fonction de la combinaison de deux ingrédients. Vous pourrez voir les tendances plus facilement et peut-être même découvrir des combinaisons de bonbon que vous n'auriez jamais pensé essayer ! À prendre en note que seules les meilleures interactions sont présentées."
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
                        "Maxime Laroche - 1950276, Félix Blanchard - 2285987, Mehdi Belchiti - 2190903, Zakaria HANIRI - 2187461, Abdellatif KTAIB - 2212233, Juliette Arcouet - 1848701. MÉTHODOLOGIE : Nos données décrivent 85 bonbons, avec les variables suivantes : 9 variables booléennes présentent dans le menu de la visualisation 1, plus un taux de sucre, une échelle de prix et un taux de d'appréciation. Aucun calcul ni traitement des données n'a été nécessaire dans cette étude sauf pour la visualisation 4 où nous avons calculés des moyennes."
                    ),
                ]
            ),
        ],
    )
