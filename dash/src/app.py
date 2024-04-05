# -*- coding: utf-8 -*-

"""
    File name: app.py
    Author: Olivia Gélinas
    Course: INF8808
    Python Version: 3.8

    This file is the entry point for our dash app.
"""

import dash
from dash import html
from dash import dcc
from dash.exceptions import PreventUpdate
import dash_bootstrap_components as dbc
from dash import Input, Output, callback

import pandas as pd

import preprocess
import viz1.viz1 as viz1
import template
from viz_container import set_layout, CANDY_TYPES
from preprocess import preprocess_data


app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
app.title = "Candy power Ranking"

df = pd.read_csv(
    "https://raw.githubusercontent.com/fivethirtyeight/data/master/candy-power-ranking/candy-data.csv"
)
df = preprocess_data(df)


template.create_custom_theme()
# template.set_default_theme()

set_layout(app, df, [viz1])


@callback(Output("viz1-1", "figure"), Input("type-menu", "value"))
def update_figure(selected_types):
    selected_types = set(CANDY_TYPES).difference(selected_types)
    if len(selected_types) == 0:
        return viz1.get_figure(df)

    filtered_df = df[sum(df[t] for t in selected_types) == 0]
    return viz1.get_figure(filtered_df)
