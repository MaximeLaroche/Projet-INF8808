"""
    Contains some functions related to the creation of the heatmap.
"""

import plotly.express as px
import hover_template
import pandas as pd


def get_figure(data: pd.DataFrame):
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
    fig = px.imshow(
        data,
        #color_continuous_scale="greens",
        labels={"x": "Year", "y": "Neighborhood"},
    )
    fig.update_layout(dragmode=False)
    fig.update_traces(hovertemplate=hover_template.get_heatmap_hover_template())
    fig.update_xaxes(dtick=1)
    # fig.show()
    return fig
