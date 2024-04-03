# -*- coding: utf-8 -*-

"""
    File name: app.py
    Author: Olivia Gélinas
    Course: INF8808
    Python Version: 3.8

    This file is the entry point for our dash app.
"""

import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output

import pandas as pd

import preprocess
import viz1.viz1 as viz1
import template


app = dash.Dash(__name__)
app.title = "Candy power Ranking"

df = pd.read_csv("assets/data/candy-data.csv")
df["sugarpercent"] *= 100
df["pricepercent"] *= 100


template.create_custom_theme()
template.set_default_theme()

app.layout = html.Div(
    className="content",
    children=[
        html.Header(
            children=[
                html.H1(app.title),
            ]
        ),
        html.Main(
            id="viz1",
            className="viz-container",
            children=[
                dcc.Graph(
                    id="heatmap",
                    className="graph",
                    figure=viz1.get_figure(df),
                    config=dict(
                        scrollZoom=False,
                        showTips=False,
                        showAxisDragHandles=False,
                        doubleClick=False,
                        displayModeBar=False,
                    ),
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
                html.Table(
                    children=[
                        html.Tr(
                            children=[
                                html.Td("Maxime Laroche"),
                                html.Td("1950276"),
                            ]
                        ),
                        html.Tr(
                            children=[
                                html.Td("Félix Blanchard"),
                                html.Td("2285987"),
                            ]
                        ),
                        html.Tr(
                            children=[
                                html.Td("Juliette Arcouet"),
                                html.Td("1848701"),
                            ]
                        ),
                        html.Tr(
                            children=[
                                html.Td("Abdellatif KTAIB"),
                                html.Td("2212233"),
                            ]
                        ),
                        html.Tr(
                            children=[
                                html.Td("Zakaria HANIRI"),
                                html.Td("2187461"),
                            ]
                        ),
                    ]
                ),
            ]
        ),
    ],
)


@app.callback(Output("line-chart", "figure"), [Input("heatmap", "clickData")])
def heatmap_clicked(click_data):
    """
    When a cell in the heatmap is clicked, updates the
    line chart to show the data for the corresponding
    neighborhood and year. If there is no data to show,
    displays a message.

    Args:
        The necessary inputs and states to update the
        line chart.
    Returns:
        The necessary output values to update the line
        chart.
    """
    if click_data is None or click_data["points"][0]["z"] == 0:
        fig = viz1_2.get_empty_figure()
        viz1_2.add_rectangle_shape(fig)
        return fig

    arrond = click_data["points"][0]["y"]
    year = click_data["points"][0]["x"]

    line_data = preprocess.get_daily_info(dataframe, arrond, year)

    line_fig = viz1_2.get_figure(line_data, arrond, year)

    return line_fig
