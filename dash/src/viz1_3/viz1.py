import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

from viz1_3.common import to_final


def get_figure(df: pd.DataFrame):
    # constants
    legend_dict = {0: "Abordable/Santé &<br>Pas apprécié", 1: "Chère/Sucré &<br> Pas apprécié",
                   2: "Abordable/Santé &<br>Apprécié", 3: "Chère/Sucré &<br>Apprécié"}
    x_col1 = "pricepercent"
    x_col2 = "sugarpercent"
    y_col = "winpercent"

    # Creating the left win / price Graph Data
    filtered1_df = df.copy()
    filtered1_df["couleur"] = (2 * (df[y_col] > 50) + (df[x_col1] > 50))
    filtered1_df = filtered1_df.sort_values("couleur", ascending=False)
    filtered1_df['index'] = filtered1_df.groupby('couleur').cumcount()

    # Creating the right win / sugar Graph Data
    filtered2_df = df.copy()
    filtered2_df["couleur"] = (2 * (df[y_col] > 50) + (df[x_col2] > 50))
    filtered2_df = filtered2_df
    filtered2_df['index'] = filtered2_df.groupby('couleur').cumcount()

    filtered2_df = filtered2_df.merge(filtered1_df[["competitorname", "couleur", "index"]].rename(
            columns={"couleur": "other_c", "index": "other_i"}
    ), on="competitorname").sort_values(["couleur", 'index'], ascending=True)
    filtered1_df = filtered1_df.merge(filtered2_df[["competitorname", "couleur", "index"]].rename(
            columns={"couleur": "other_c", "index": "other_i"}
    ), on="competitorname").sort_values(["couleur", 'index'], ascending=True)

    # Replace number for correct label
    filtered1_df["couleur"] = filtered1_df["couleur"].map(legend_dict)
    filtered2_df["couleur"] = filtered2_df["couleur"].map(legend_dict)

    # Creating the Graphs
    color_map = {
        legend_dict[0]: '#636EFA', legend_dict[1]: '#B82E2E', legend_dict[2]: '#00CC96', legend_dict[3]: '#FF7F0E'
    }
    scat1 = px.scatter(filtered1_df, x=x_col1, y=y_col, hover_data=["competitorname", "other_c", "other_i"],
                       color="couleur", color_discrete_map=color_map)
    scat2 = px.scatter(filtered2_df, x=x_col2, y=y_col, hover_data=["competitorname", "other_c", "other_i"],
                       color="couleur", color_discrete_map=color_map)

    # creating the final graph
    return to_final(scat1, scat2)


