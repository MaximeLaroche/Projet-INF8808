import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

from viz1_3.common import to_final


def get_figure(df: pd.DataFrame):
    # constants
    legend_list = ["chocolate", "fruity", "caramel", "peanutyalmondy",
                   "nougat", "crispedricewafer", "hard", "bar", "pluribus"]
    legend_names = {"chocolate": "chocolate", "fruity": "fruity", "caramel": "caramel",
                    "peanutyalmondy": "peanuty & almondy", "nougat": "nougat", "crispedricewafer": "crisped rice wafer",
                    "hard": "hard", "bar": "bar", "pluribus": "pluribus"}

    x_col1 = "pricepercent"
    x_col2 = "sugarpercent"
    y_col = "winpercent"

    # Creating the left win / price Graph Data
    filtered1_df = df.copy()
    filtered1_df = pd.melt(filtered1_df, id_vars=['competitorname', y_col, x_col1, x_col2], value_vars=legend_list)
    filtered1_df = filtered1_df[filtered1_df['value']]\
        .rename(columns={'variable': 'couleur'})\
        .drop(columns=['value'])

    type_order = filtered1_df[['couleur', 'competitorname']]\
        .groupby('couleur')\
        .count()\
        .reset_index()\
        .sort_values('competitorname')['couleur']\
        .tolist()

    map_dict = {v: i for i, v in enumerate(type_order)}
    legend_dict = {i: legend_names[v] for i, v in enumerate(type_order)}

    filtered1_df["couleur"] = filtered1_df["couleur"].map(map_dict)
    filtered1_df = filtered1_df.sort_values("couleur", ascending=False)

    # Replace number for correct label
    filtered1_df["couleur"] = filtered1_df["couleur"].map(legend_dict)

    scat1 = px.scatter(filtered1_df, x=x_col1, y=y_col, hover_data=["competitorname"], color="couleur")
    scat2 = px.scatter(filtered1_df, x=x_col2, y=y_col, hover_data=["competitorname"], color="couleur")

    # creating the final graph
    return to_final(scat1, scat2)
