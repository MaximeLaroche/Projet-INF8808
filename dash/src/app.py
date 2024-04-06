# -*- coding: utf-8 -*-

"""
    File name: app.py
    Author: Olivia Gélinas
    Course: INF8808
    Python Version: 3.8

    This file is the entry point for our dash app.
"""

import dash
from dash import Input, Output, callback

import pandas as pd
import numpy as np

import viz1_3.viz1 as viz1
import viz1_3.viz2 as viz2
import template
from viz_container import set_layout, CANDY_TYPES
from preprocess import preprocess_data


app = dash.Dash(__name__)
app.title = "Candy power Ranking"

df = pd.read_csv("https://raw.githubusercontent.com/fivethirtyeight/data/master/candy-power-ranking/candy-data.csv")
df = preprocess_data(df)


template.create_custom_theme()
template.set_default_theme()

set_layout(app, df, [viz1, viz2])


@callback(
    Output('viz1-graph', 'figure'),
    Input('candy-type-menu', 'value')
)
def update_vis(selected_types):
    filtered_df = df[sum(df[t] for t in selected_types) > 0]
    return viz1.get_figure(filtered_df)


@callback(
    Output('viz2-graph', 'figure'),
    Input('candy-choice-menu', 'value'),
    Input('candy-proximity', 'value')
)
def update_vis2(selected_candy, proximity_val):
    if selected_candy is None:
        return viz2.get_figure(df)

    types = [r['value'] for r in CANDY_TYPES]

    _df = df.copy()
    values: pd.Series = _df[_df['competitorname'] == selected_candy][types].iloc[0]

    def proximity(row):
        return np.sum(row == values)

    _df['proximity'] = _df[types].apply(proximity, axis=1)
    filtered_df = _df[_df['proximity'] >= proximity_val]

    return viz2.get_figure(filtered_df)
