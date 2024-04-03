from plotly.subplots import make_subplots
import plotly.graph_objects as go


"""
Note :beaucoup d'info pertinente pour avoir des légendes ou axe commune entre deux sous graphique utilie ici https://plotly.com/python/subplots/
"""

fig = make_subplots(
    rows=4,
    cols=2,
    specs=[
        [{}, {}],
        [{}, {}],
        [{}, {}],
        [{"rowspan": 1, "colspan": 2}, None],
    ],
    print_grid=True,
)


fig.add_trace(go.Scatter(x=[1, 2], y=[1, 2], name="(1,1)"), row=1, col=1)
fig.add_trace(go.Scatter(x=[1, 2], y=[1, 2], name="(1,2)"), row=1, col=2)

fig.add_trace(go.Scatter(x=[1, 2], y=[1, 2], name="(2,1)"), row=2, col=1)
fig.add_trace(go.Scatter(x=[1, 2], y=[1, 2], name="(3,1)"), row=2, col=2)

fig.add_trace(go.Scatter(x=[1, 2], y=[1, 2], name="(2,1)"), row=3, col=1)
fig.add_trace(go.Scatter(x=[1, 2], y=[1, 2], name="(3,1)"), row=3, col=2)

fig.add_trace(go.Scatter(x=[1, 2], y=[1, 2], name="(3,1)"), row=4, col=1)

fig.update_layout(title_text="specs examples")
fig.show()
