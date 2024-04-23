import plotly.express as px
import pandas as pd
from itertools import combinations
from plotly import subplots
import plotly.graph_objects as go


COLUMNS = ['crispedricewafer', 'peanutyalmondy', 'chocolate', 'nougat', 'caramel', 'fruity']
COL_STR = {"chocolate": "chocolate", "fruity": "fruity", "caramel": "caramel",
                "peanutyalmondy": "peanuty & almondy", "nougat": "nougat", "crispedricewafer": "crisped rice wafer",
                "hard": "hard", "bar": "bar", "pluribus": "pluribus"}
POPULAR_MIX = [
    ('caramel', 'crispedricewafer'),
    ('chocolate', 'peanutyalmondy'),
    ('caramel', 'nougat'),
    ('chocolate', 'crispedricewafer'),
    ('chocolate', 'caramel'),
    ('caramel', 'peanutyalmondy'),
]


def get_figures(df: pd.DataFrame):

    # Chargement des données
    dfs = {}
    col_means = {}
    for col in COLUMNS:
        dfs[col] = df[df[col] == 1]
        col_means[col] = dfs[col]['winpercent'].mean()

    subplot_titles = [f'{COL_STR[col]}' for col in COLUMNS]
    fig = make_subplot(subplot_titles, dfs, col_means, COLUMNS, [0, 15])

    # Second part on interaction
    mix_dfs = {}
    mix_col_means = {}
    for col1, col2 in combinations(COLUMNS, 2):
        key = tuple(sorted([col1, col2]))
        mix_dfs[key] = dfs[col1][dfs[col1][col2] == 1]
        mix_col_means[key] = mix_dfs[key]['winpercent'].mean()

    mix_keys = [tuple(sorted([col1, col2])) for col1, col2 in POPULAR_MIX]
    subplot_titles = [f'{COL_STR[col1]} - {COL_STR[col2]}' for col1, col2 in mix_keys]
    mix_fig = make_subplot(subplot_titles, mix_dfs, mix_col_means, mix_keys, [0, 8])

    return fig, mix_fig


def make_subplot(titles, dfs, means, keys, y_range):
    fig = subplots.make_subplots(rows=2, cols=3, subplot_titles=titles)
    for i, key in enumerate(keys):
        fig.add_trace(
            go.Histogram(x=dfs[key]['winpercent'], xbins=dict(start=0, end=100, size=10)),
            row=i // 3 + 1, col=i % 3 + 1
        )

        fig.add_vline(
            x=means[key],
            line_dash="dash",
            line_color="dimgrey",
            annotation_text="Moyenne de " + str(round(means[key], 1)),
            annotation_font_size=20,
            annotation_font_color="dimgrey",
            row=i // 3 + 1, col=i % 3 + 1
        )

    fig.update_xaxes(title="Taux d'appréciation", range=[0, 100])
    fig.update_yaxes(title='Quantité de Bonbons', range=y_range)
    fig.update_layout(showlegend=False)
    fig.update_traces(marker_color='royalblue', hoverinfo="skip")
    return fig
