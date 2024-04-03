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
from viz_container import set_layout
from preprocess import preprocess_data


app = dash.Dash(__name__)
app.title = "Candy power Ranking"

df = pd.read_csv(
    "https://raw.githubusercontent.com/fivethirtyeight/data/master/candy-power-ranking/candy-data.csv"
)
df = preprocess_data(df)


template.create_custom_theme()
template.set_default_theme()

set_layout(app, df, [viz1])
