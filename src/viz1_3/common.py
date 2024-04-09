import plotly.graph_objects as go


TEMPLATE_NAME = 'simple_white'


def to_final(right: go.Figure, left: go.Figure):
    left.update_traces(xaxis="x2", yaxis="y2", showlegend=False)
    fig = go.Figure(
        # putting the figures in order. Text must be first to be behind the layer of the Data
        data=[*right.data, *left.data],
        layout=get_layout()
    )
    # Changing the hover_template for all graphs
    fig.update_traces(hovertemplate=(
        '<b style="font-size: 1.3em">%{customdata[0]}</b><br>'
        'Appréciation (%): %{y}<br>'
        '%{xaxis.title.text}: %{x}<br>'
        '<extra></extra>'
    ), selector=dict(type="scatter", mode="markers"))

    # making sure it's impossible to hover over the text
    [fig.add_trace(t) for t in get_text()]
    fig.update_traces(hoverinfo="skip", selector=dict(type="scatter", mode="text"))

    return fig


def get_text():
    return [
        # Text Right Graph
        go.Scatter(
            x=[25], y=[94], mode="text",
            text='<b style="color:grey; font-size:1.3em">Abordable & Apprécié</b>',
            textposition="middle center", textfont_color="rgba(80,80,80,0.6)",
            xaxis="x", yaxis="y", showlegend=False
        ),
        go.Scatter(
            x=[25], y=[44], mode="text",
            text='<b style="color:grey; font-size:1.3em">Abordable & Pas apprécié</b>',
            textposition="middle center", textfont_color="rgba(80,80,80,0.6)",
            xaxis="x", yaxis="y", showlegend=False
        ),
        go.Scatter(
            x=[75], y=[94], mode="text",
            text='<b style="color:grey; font-size:1.3em">Chère & Apprécié</b>',
            textposition="middle center", textfont_color="rgba(80,80,80,0.6)",
            xaxis="x", yaxis="y", showlegend=False
        ),
        go.Scatter(
            x=[75], y=[44], mode="text",
            text='<b style="color:grey; font-size:1.3em">Chère & Pas apprécié</b>',
            textposition="middle center", textfont_color="rgba(80,80,80,0.6)",
            xaxis="x", yaxis="y", showlegend=False
        ),

        # Text Left Graph
        go.Scatter(
            x=[25], y=[94], mode="text",
            text='<b style="color:grey; font-size:1.3em">Santé & Apprécié</b>',
            textposition="middle center", textfont_color="rgba(80,80,80,0.6)",
            showlegend=False, xaxis="x2", yaxis="y2",
        ),
        go.Scatter(
            x=[25], y=[44], mode="text",
            text='<b style="color:grey; font-size:1.3em">Santé & Pas apprécié</b>',
            textposition="middle center", textfont_color="rgba(80,80,80,0.6)",
            showlegend=False, xaxis="x2", yaxis="y2",
        ),
        go.Scatter(
            x=[75], y=[94], mode="text",
            text='<b style="color:grey; font-size:1.3em">Sucré & Apprécié</b>',
            textposition="middle center", textfont_color="rgba(80,80,80,0.6)",
            showlegend=False, xaxis="x2", yaxis="y2",
        ),
        go.Scatter(
            x=[75], y=[44], mode="text",
            text='<b style="color:grey; font-size:1.3em">Sucré & Pas apprécié</b>',
            textposition="middle center", textfont_color="rgba(80,80,80,0.6)",
            showlegend=False, xaxis="x2", yaxis="y2",
        ),
    ]


def get_layout():
    return {
        # Adding the 4 axix for the two graphs
        "xaxis": {"anchor": "y", "domain": [0, 0.49], "range": [0, 100], "title": {"text": "Prix relatif (%)"}},
        "xaxis2": {"anchor": "y2", "domain": [0.51, 1], "range": [0, 100], "matches": "x",
                   "title": {"text": "Proportion de sucre (%)"}},
        "yaxis": {"anchor": "x", "domain": [0, 1], "range": [0, 100], "title": {"text": "Appréciation (%)"}},
        "yaxis2": {"anchor": "x2", "domain": [0, 1], "range": [0, 100], "matches": "y", "showticklabels": False},
        # Adding the 4 lines to divide the graph into four parts
        "shapes": [
            {"layer": "below", "line": {"color": "grey", "width": 2}, "type": "line",
             "x0": 50, "x1": 50, "xref": "x", "y0": 0, "y1": 1, "yref": "y domain"},
            {"layer": "below", "line": {"color": "grey", "width": 2}, "type": "line",
             "x0": 50, "x1": 50, "xref": "x2", "y0": 0, "y1": 1, "yref": "y2 domain"},
            {"layer": "below", "line": {"color": "grey", "width": 2}, "type": "line",
             "x0": 0, "x1": 1, "xref": "x domain", "y0": 50, "y1": 50, "yref": "y"},
            {"layer": "below", "line": {"color": "grey", "width": 2}, "type": "line",
             "x0": 0, "x1": 1, "xref": "x2 domain", "y0": 50, "y1": 50, "yref": "y2"},
        ],
        #'grid': {'rows': 1, 'columns': 2, 'pattern': 'independent', columnorder: 'bottom to top'}
        # Adding the Legend
        "legend": {"itemsizing": "constant", "orientation": "h", "title": {"text": ""},
                   "tracegroupgap": 0, "x": 0.5, "xanchor": "center", "y": 1.03, "yanchor": "bottom"},
        "template": TEMPLATE_NAME,
    }
