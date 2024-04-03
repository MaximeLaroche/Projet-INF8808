"""
    Contains some functions related to the creation of the heatmap.
"""

import plotly.express as px
import plotly.graph_objects as go
import pandas as pd


def get_figure(df: pd.DataFrame):
    """
    Generates the heatmap from the given dataset.

    Make sure to set the title of the color bar to 'Trees'
    and to display each year as an x-tick. The x and y axes should
    be titled "Year" and "Neighborhood".

    Args:
        data: The data to display
    Returns:
        The figure to be displayed.
    """

    # TODO : Create the heatmap. Make sure to set dragmode=False in
    x_col1 = "pricepercent"
    x_col2 = "sugarpercent"
    y_col = "winpercent"

    filtered1_df = df.copy()
    filtered1_df["couleur"] = (2 * (df["winpercent"] > 50) + (df[x_col1] > 50)).map(
        {
            0: "Abordable/Santé &<br>Pas apprécié",
            1: "Abordable/Santé &<br>Apprécié",
            2: "Chère/Sucré &<br>Pas apprécié",
            3: "Chère/Sucré &<br>Apprécié",
        }
    )
    filtered1_df = filtered1_df.sort_values("couleur", ascending=False)

    filtered2_df = df.copy()
    filtered2_df["couleur"] = (2 * (df["winpercent"] > 50) + (df[x_col2] > 50)).map(
        {
            0: "Abordable/Santé &<br>Pas apprécié",
            1: "Abordable/Santé &<br>Apprécié",
            2: "Chère/Sucré &<br>Pas apprécié",
            3: "Chère/Sucré &<br>Apprécié",
        }
    )
    filtered2_df = filtered2_df.sort_values("couleur", ascending=False)

    scat1 = px.scatter(
        filtered1_df,
        x=x_col1,
        y=y_col,
        color="couleur",
        hover_data=["competitorname"],
        template="simple_white",
    )

    scat2 = px.scatter(
        filtered2_df,
        x=x_col2,
        y=y_col,
        color="couleur",
        hover_data=["competitorname"],
        template="simple_white",
    )
    scat2.update_traces(xaxis="x2")
    scat2.update_traces(yaxis="y2")
    scat2.update_traces(showlegend=False)
    # scat2.for_each_trace(lambda x: x.update(legendgroup=x['legendgroup'] + '-1'))

    text = [
        # Text Right Graph
        go.Scatter(
            x=[25],
            y=[94],
            mode="text",
            text='<b style="color:grey; font-size:1.3em">Abordable & Apprécié</b>',
            textposition="middle center",
            textfont_color="rgba(80,80,80,0.6)",
            showlegend=False,
            xaxis="x",
            yaxis="y",
        ),
        go.Scatter(
            x=[25],
            y=[44],
            mode="text",
            text='<b style="color:grey; font-size:1.3em">Abordable & Pas apprécié</b>',
            textposition="middle center",
            textfont_color="rgba(80,80,80,0.6)",
            showlegend=False,
            xaxis="x",
            yaxis="y",
        ),
        go.Scatter(
            x=[75],
            y=[94],
            mode="text",
            text='<b style="color:grey; font-size:1.3em">Chère & Apprécié</b>',
            textposition="middle center",
            textfont_color="rgba(80,80,80,0.6)",
            showlegend=False,
            xaxis="x",
            yaxis="y",
        ),
        go.Scatter(
            x=[75],
            y=[44],
            mode="text",
            text='<b style="color:grey; font-size:1.3em">Chère & Pas apprécié</b>',
            textposition="middle center",
            textfont_color="rgba(80,80,80,0.6)",
            showlegend=False,
            xaxis="x",
            yaxis="y",
        ),
        # Text Left Graph
        go.Scatter(
            x=[25],
            y=[94],
            mode="text",
            text='<b style="color:grey; font-size:1.3em">Santé & Apprécié</b>',
            textposition="middle center",
            textfont_color="rgba(80,80,80,0.6)",
            showlegend=False,
            xaxis="x2",
            yaxis="y2",
        ),
        go.Scatter(
            x=[25],
            y=[44],
            mode="text",
            text='<b style="color:grey; font-size:1.3em">Santé & Pas apprécié</b>',
            textposition="middle center",
            textfont_color="rgba(80,80,80,0.6)",
            showlegend=False,
            xaxis="x2",
            yaxis="y2",
        ),
        go.Scatter(
            x=[75],
            y=[94],
            mode="text",
            text='<b style="color:grey; font-size:1.3em">Sucré & Apprécié</b>',
            textposition="middle center",
            textfont_color="rgba(80,80,80,0.6)",
            showlegend=False,
            xaxis="x2",
            yaxis="y2",
        ),
        go.Scatter(
            x=[75],
            y=[44],
            mode="text",
            text='<b style="color:grey; font-size:1.3em">Sucré & Pas apprécié</b>',
            textposition="middle center",
            textfont_color="rgba(80,80,80,0.6)",
            showlegend=False,
            xaxis="x2",
            yaxis="y2",
        ),
    ]

    fig = go.Figure(
        [*text, *scat1.data, *scat2.data],
        layout={
            "xaxis": {
                "anchor": "y",
                "domain": [0, 0.49],
                "range": [0, 100],
                "title": {"text": "Prix relatif (%)"},
            },
            "xaxis2": {
                "anchor": "y2",
                "domain": [0.51, 1],
                "range": [0, 100],
                "matches": "x",
                "title": {"text": "Proportion de sucre (%)"},
            },
            "yaxis": {
                "anchor": "x",
                "domain": [0, 1],
                "range": [0, 100],
                "title": {"text": "Appréciation (%)"},
            },
            "yaxis2": {
                "anchor": "x2",
                "domain": [0, 1],
                "range": [0, 100],
                "matches": "y",
                "showticklabels": False,
            },
            "shapes": [
                {
                    "layer": "below",
                    "line": {"color": "grey", "width": 2},
                    "type": "line",
                    "x0": 50,
                    "x1": 50,
                    "xref": "x",
                    "y0": 0,
                    "y1": 1,
                    "yref": "y domain",
                },
                {
                    "layer": "below",
                    "line": {"color": "grey", "width": 2},
                    "type": "line",
                    "x0": 50,
                    "x1": 50,
                    "xref": "x2",
                    "y0": 0,
                    "y1": 1,
                    "yref": "y2 domain",
                },
                {
                    "layer": "below",
                    "line": {"color": "grey", "width": 2},
                    "type": "line",
                    "x0": 0,
                    "x1": 1,
                    "xref": "x domain",
                    "y0": 50,
                    "y1": 50,
                    "yref": "y",
                },
                {
                    "layer": "below",
                    "line": {"color": "grey", "width": 2},
                    "type": "line",
                    "x0": 0,
                    "x1": 1,
                    "xref": "x2 domain",
                    "y0": 50,
                    "y1": 50,
                    "yref": "y2",
                },
            ],
            "legend": {
                "itemsizing": "constant",
                "orientation": "h",
                "title": {"text": ""},
                "tracegroupgap": 0,
                "x": 0.5,
                "xanchor": "center",
                "y": 1.03,
                "yanchor": "bottom",
            },
            #'legend' : {'itemsizing': 'constant', 'orientation': 'h', 'title': {'text': ''}, 'tracegroupgap': 0, 'x': 0.25, 'xanchor': 'center', 'y': 1.03, 'yanchor': 'bottom'},
            # 'legend2': {'itemsizing': 'constant', 'orientation': 'h', 'title': {'text': ''}, 'tracegroupgap': 0, 'x': 0.75, 'xanchor': 'center', 'y': 1.03, 'yanchor': 'bottom'},
            "template": "simple_white",
        },
    )

    fig.update_traces(
        hovertemplate="""
    <b style="font-size: 1.3em">%{customdata}</b><br>
    %{yaxis.title.text}: %{y}<br>
    %{xaxis.title.text}: %{x}<br>
    <extra></extra>
    """,
        selector=dict(type="scatter", mode="markers"),
    )
    fig.update_traces(hoverinfo="skip", selector=dict(type="scatter", mode="text"))
    return fig
