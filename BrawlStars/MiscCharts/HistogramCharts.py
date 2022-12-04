import pandas
import plotly.express as px


def histogram_chart_by_hero_parity():
    df = pandas.read_csv('BrawlStars.csv')
    fig = px.histogram(df, x="Hero Rarity", y="Trophies", title="Hero by Parity in Histogram",
                       barmode='group', color="Trophies")
    # fig.show() # for debug
    return fig


def histogram_chart_by_hero_class():
    df = pandas.read_csv('BrawlStars.csv')
    fig = px.histogram(df, x="Hero Class", y="Trophies", title="Hero by Class in Histogram",
                       barmode='group', color="Trophies", histfunc='max')
    # fig.show() # for debug
    return fig
