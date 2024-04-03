"""
    Contains some functions related to the creation of the line chart.
"""

import plotly.express as px
import hover_template
import plotly.graph_objects as go
from template import THEME


def get_empty_figure():
    """
    Returns the figure to display when there is no data to show.

    The text to display is : 'No data to display. Select a cell
    in the heatmap for more information.

    """

    # TODO : Construct the empty figure to display. Make sure to
    # set dragmode=False in the layout.
    fig = go.Figure()
    fig.update_layout(showlegend=False)
    fig.update_xaxes(visible=False)
    fig.update_yaxes(visible=False)

    fig.add_annotation(text="No data to display. Select a cell in the heatmap for more information", showarrow=False)
    fig.update_layout(dragmode=False)
    return fig


def add_rectangle_shape(fig):
    """
    Adds a rectangle to the figure displayed
    behind the informational text. The color
    is the 'pale_color' in the THEME dictionary.

    The rectangle's width takes up the entire
    paper of the figure. The height goes from
    0.25% to 0.75% the height of the figure.
    """
    # TODO : Draw the rectangle
    fig: go.Figure
    w = fig.layout.width
    h = fig.layout.height

    fig.add_shape(
        type="rect",
        xref="x", yref="y",
        x0=-1, y0=0,
        x1=6, y1=3,
        line=dict(color=THEME['pale_color'], width=3),
        fillcolor=THEME['pale_color']
    )


def get_figure(line_data, arrond, year):
    """
    Generates the line chart using the given data.

    The ticks must show the zero-padded day and
    abbreviated month. The y-axis title should be 'Trees'
    and the title should indicated the displayed
    neighborhood and year.

    In the case that there is only one data point,
    the trace should be displayed as a single
    point instead of a line.

    Args:
        line_data: The data to display in the
        line chart
        arrond: The selected neighborhood
        year: The selected year
    Returns:
        The figure to be displayed
    """
    # TODO : Construct the required     figure. Don't forget to include the hover template

    fig = px.line(
        line_data,
        x='Date_Plantation',
        y='Arrond',
        markers=line_data.shape[0] <= 1,
        title=f'Trees planted in {arrond} in {year}',
        labels={"Date_Plantation": "", "Arrond": "Trees"},
        color_discrete_sequence=['black']
    )
    fig.update_layout(xaxis=dict(tickformat="%d %b"))
    fig.update_traces(hovertemplate=hover_template.get_linechart_hover_template())

    return fig

