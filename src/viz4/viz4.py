import plotly.express as px
import pandas as pd
from plotly.subplots import make_subplots
import plotly.graph_objects as go


aliments = []
combo_aliments = []

# Chargement des données
df = pd.read_csv("https://raw.githubusercontent.com/fivethirtyeight/data/master/candy-power-ranking/candy-data.csv")
df_chocolate = df[df['chocolate'] == 1]
chocolate_mean = df_chocolate['winpercent'].mean()

df_fruity = df[df['fruity'] == 1]
fruity_mean = df_fruity['winpercent'].mean()

df_caramel = df[df['caramel'] == 1]
caramel_mean = df_caramel['winpercent'].mean()

df_peanutyalmondy = df[df['peanutyalmondy'] == 1]
peanutyalmondy_mean = df_peanutyalmondy['winpercent'].mean()

df_crispedricewafer = df[df['crispedricewafer'] == 1]
crispedricewafer_mean = df_crispedricewafer['winpercent'].mean()

df_nougat = df[df['nougat'] == 1]
nougat_mean = df_nougat['winpercent'].mean()

# fig4_ 1
fig4_1 = px.histogram(df_fruity, x='winpercent', nbins=5, title='Fruity', height=500, width=500)

fig4_1.update_layout(
    plot_bgcolor='whitesmoke',
    title=dict(
        text='Fruity',
        x=0.5
    )
)
fig4_1.update_traces(marker_color='royalblue')

fig4_1.add_vline(x=fruity_mean, line_dash="dash", line_color="dimgrey", annotation_text="Moyenne de " + str(round(fruity_mean, 1)), 
            annotation_font_size=20,
            annotation_font_color="dimgrey")

fig4_1.update_xaxes(title="Taux d'appréciation", range=[0, 100])
fig4_1.update_yaxes(title='Quantité de Bonbons', range=[0, 15])

# fig4_ 2
fig4_2 = px.histogram(df_chocolate, x='winpercent', nbins=5, title='Chocolate', height=500, width=500)

fig4_2.update_layout(
    plot_bgcolor='whitesmoke',
    title=dict(
        text='Chocolate',
        x=0.5
    )
)

fig4_2.update_traces(marker_color='royalblue')

fig4_2.add_vline(x=chocolate_mean, line_dash="dash", line_color="dimgrey", annotation_text="Moyenne de " + str(round(chocolate_mean, 1)), 
            annotation_font_size=20,
            annotation_font_color="dimgrey")

fig4_2.update_xaxes(title="Taux d'appréciation", range=[0, 100])
fig4_2.update_yaxes(title='Quantité de Bonbons', range=[0, 15])


# fig4_ 3
fig4_3 = px.histogram(df_caramel, x='winpercent', nbins=5, height=500, width=500)

fig4_3.update_layout(
    plot_bgcolor='whitesmoke',
    title=dict(
        text='Caramel',
        x=0.5
    )
)
fig4_3.update_traces(marker_color='royalblue')

fig4_3.add_vline(x=caramel_mean , line_dash="dash", line_color="dimgrey", annotation_text="Moyenne de " + str(round(caramel_mean , 1)), 
            annotation_font_size=20,
            annotation_font_color="dimgrey")

fig4_3.update_xaxes(title="Taux d'appréciation", range=[0, 100])
fig4_3.update_yaxes(title='Quantité de Bonbons', range=[0, 15])


# fig4_ 4
fig4_4 = px.histogram(df_peanutyalmondy, x='winpercent', nbins=10, height=500, width=500)

fig4_4.update_layout(
    plot_bgcolor='whitesmoke',
    title=dict(
        text='Peanutyalmondy',
        x=0.5
    )
)
fig4_4.update_traces(marker_color='royalblue')

fig4_4.add_vline(x=peanutyalmondy_mean , line_dash="dash", line_color="dimgrey", annotation_text="Moyenne de " + str(round(peanutyalmondy_mean , 1)), 
            annotation_font_size=20,
            annotation_font_color="dimgrey")

fig4_4.update_xaxes(title="Taux d'appréciation", range=[0, 100])
fig4_4.update_yaxes(title='Quantité de Bonbons', range=[0, 15])

# fig4_ 5
fig4_5 = px.histogram(df_crispedricewafer, x='winpercent', nbins=5, height=500, width=500)

fig4_5.update_layout(
    plot_bgcolor='whitesmoke',
    title=dict(
        text='Crispedricewafer ',
        x=0.5
    )
)
fig4_5.update_traces(marker_color='royalblue')

fig4_5.add_vline(x=crispedricewafer_mean, line_dash="dash", line_color="dimgrey", annotation_text="Moyenne de " + str(round(crispedricewafer_mean, 1)), 
            annotation_font_size=20,
            annotation_font_color="dimgrey")

fig4_5.update_xaxes(title="Taux d'appréciation", range=[0, 100])
fig4_5.update_yaxes(title='Quantité de Bonbons', range=[0, 15])

# fig4_ 6
fig4_6 = px.histogram(df_nougat , x='winpercent', nbins=5, height=500, width=500)

fig4_6.update_layout(
    plot_bgcolor='whitesmoke',
    title=dict(
        text='Nougat ',
        x=0.5
    )
)
fig4_6.update_traces(marker_color='royalblue')

fig4_6.add_vline(x=nougat_mean, line_dash="dash", line_color="dimgrey", annotation_text="Moyenne de " + str(round(nougat_mean, 1)), 
            annotation_font_size=20,
            annotation_font_color="dimgrey")

fig4_6.update_xaxes(title="Taux d'appréciation", range=[0, 100])
fig4_6.update_yaxes(title='Quantité de Bonbons', range=[0, 15])

# Second part on interaction
df_chocolate_caramel = df_chocolate[df_chocolate['caramel'] == 1]
df_chocolate_caramel_mean = df_chocolate_caramel['winpercent'].mean()

df_chocolate_fruity = df_chocolate[df_chocolate['fruity'] == 1]
df_chocolate_fruity_mean = df_chocolate_fruity['winpercent'].mean()

df_chocolate_peanut = df_chocolate[df_chocolate['peanutyalmondy'] == 1]
df_chocolate_peanut_mean = df_chocolate_peanut['winpercent'].mean()

df_chocolate_nougat = df_chocolate[df_chocolate['nougat'] == 1]
df_chocolate_nougat_mean = df_chocolate_nougat['winpercent'].mean()

df_chocolate_crispe = df_chocolate[df_chocolate['crispedricewafer'] == 1]
df_chocolate_crispe_mean = df_chocolate_crispe['winpercent'].mean()


df_fruity_caramel = df_fruity[df_fruity['caramel'] == 1]
df_fruity_caramel_mean = df_fruity_caramel['winpercent'].mean()

df_fruity_peanut = df_fruity[df_fruity['peanutyalmondy'] == 1]
df_fruity_peanut_mean = df_fruity_peanut['winpercent'].mean()

df_fruity_nougat = df_fruity[df_fruity['nougat'] == 1]
df_fruity_nougat_mean = df_fruity_nougat['winpercent'].mean()

df_fruity_crispe = df_fruity[df_fruity['crispedricewafer'] == 1]
df_fruity_crispe_mean = df_fruity_crispe['winpercent'].mean()


df_caramel_peanut = df_caramel[df_caramel['peanutyalmondy'] == 1]
df_caramel_peanut_mean = df_caramel_peanut['winpercent'].mean()

df_caramel_nougat = df_caramel[df_caramel['nougat'] == 1]
df_caramel_nougat_mean = df_caramel_nougat['winpercent'].mean()

df_caramel_crispe = df_caramel[df_caramel['crispedricewafer'] == 1]
df_caramel_crispe_mean = df_caramel_crispe['winpercent'].mean()


df_peanutyalmondy_nougat = df_peanutyalmondy[df_peanutyalmondy['nougat'] == 1]
df_peanutyalmondy_nougat_mean = df_peanutyalmondy_nougat['winpercent'].mean()

df_peanutyalmondy_crispe = df_peanutyalmondy[df_peanutyalmondy['crispedricewafer'] == 1]
df_peanutyalmondy_crispe_mean = df_peanutyalmondy_crispe['winpercent'].mean()


df_nougat_crispe = df_nougat[df_nougat['crispedricewafer'] == 1]
df_nougat_crispe_mean = df_nougat_crispe['winpercent'].mean()


# fig4_ 7
fig4_7 = px.histogram(df_caramel_crispe , x='winpercent', nbins=4, height=500, width=500)

fig4_7.update_layout(
    plot_bgcolor='whitesmoke',
    title=dict(
        text='caramel_crispe',
        x=0.5
    )
)
fig4_7.update_traces(marker_color='royalblue')

fig4_7.add_vline(x=df_caramel_crispe_mean, line_dash="dash", line_color="dimgrey", annotation_text="Moyenne de " + str(round(df_caramel_crispe_mean, 1)), 
            annotation_font_size=20,
            annotation_font_color="dimgrey")

fig4_7.update_xaxes(title="Taux d'appréciation", range=[0, 100])
fig4_7.update_yaxes(title='Quantité de Bonbons', range=[0, 8])

# fig4_ 8
fig4_8 = px.histogram(df_caramel_nougat , x='winpercent', nbins=2, height=500, width=500)

fig4_8.update_layout(
    plot_bgcolor='whitesmoke',
    title=dict(
        text='caramel_nougat',
        x=0.5
    )
)
fig4_8.update_traces(marker_color='royalblue')

fig4_8.add_vline(x=df_caramel_nougat_mean, line_dash="dash", line_color="dimgrey", annotation_text="Moyenne de " + str(round(df_caramel_nougat_mean, 1)), 
            annotation_font_size=20,
            annotation_font_color="dimgrey")

fig4_8.update_xaxes(title="Taux d'appréciation", range=[0, 100])
fig4_8.update_yaxes(title='Quantité de Bonbons', range=[0, 8])

# fig4_ 9
fig4_9 = px.histogram(df_caramel_peanut , x='winpercent', nbins=2, height=500, width=500)

fig4_9.update_layout(
    plot_bgcolor='whitesmoke',
    title=dict(
        text='caramel_peanut',
        x=0.5
    )
)
fig4_9.update_traces(marker_color='royalblue')

fig4_9.add_vline(x=df_caramel_peanut_mean, line_dash="dash", line_color="dimgrey", annotation_text="Moyenne de " + str(round(df_caramel_peanut_mean, 1)), 
            annotation_font_size=20,
            annotation_font_color="dimgrey")

fig4_9.update_xaxes(title="Taux d'appréciation", range=[0, 100])
fig4_9.update_yaxes(title='Quantité de Bonbons', range=[0, 8])

# fig4_ 10
fig4_10 = px.histogram(df_chocolate_crispe , x='winpercent', nbins=5, height=500, width=500)

fig4_10.update_layout(
    plot_bgcolor='whitesmoke',
    title=dict(
        text='chocolate_crispe',
        x=0.5
    )
)
fig4_10.update_traces(marker_color='royalblue')

fig4_10.add_vline(x=df_chocolate_crispe_mean, line_dash="dash", line_color="dimgrey", annotation_text="Moyenne de " + str(round(df_chocolate_crispe_mean, 1)), 
            annotation_font_size=20,
            annotation_font_color="dimgrey")

fig4_10.update_xaxes(title="Taux d'appréciation", range=[0, 100])
fig4_10.update_yaxes(title='Quantité de Bonbons', range=[0, 8])

# fig4_ 11
fig4_11 = px.histogram(df_chocolate_peanut, x='winpercent', nbins=5, height=500, width=500)

fig4_11.update_layout(
    plot_bgcolor='whitesmoke',
    title=dict(
        text='chocolate_peanut',
        x=0.5
    )
)
fig4_11.update_traces(marker_color='royalblue')

fig4_11.add_vline(x=df_chocolate_peanut_mean, line_dash="dash", line_color="dimgrey", annotation_text="Moyenne de " + str(round(df_chocolate_peanut_mean, 1)), 
            annotation_font_size=20,
            annotation_font_color="dimgrey")

fig4_11.update_xaxes(title="Taux d'appréciation", range=[0, 100])
fig4_11.update_yaxes(title='Quantité de Bonbons', range=[0, 8])

# fig4_ 12
fig4_12 = px.histogram(df_chocolate_caramel, x='winpercent', nbins=5, height=500, width=500)

fig4_12.update_layout(
    plot_bgcolor='whitesmoke',
    title=dict(
        text='chocolate_caramel',
        x=0.5
    )
)
fig4_12.update_traces(marker_color='royalblue')

fig4_12.add_vline(x=df_chocolate_caramel_mean, line_dash="dash", line_color="dimgrey", annotation_text="Moyenne de " + str(round(df_chocolate_caramel_mean, 1)), 
            annotation_font_size=20,
            annotation_font_color="dimgrey")

fig4_12.update_xaxes(title="Taux d'appréciation", range=[0, 100])
fig4_12.update_yaxes(title='Quantité de Bonbons', range=[0, 8])


# print("Aliments les plus appréciés :")
aliments = [fig4_1, fig4_3, fig4_6, fig4_2, fig4_4, fig4_5]


# print("Combinaison d'aliments les plus appréciés :")
combo_aliments = [fig4_9, fig4_12, fig4_10, fig4_8, fig4_11, fig4_7]

