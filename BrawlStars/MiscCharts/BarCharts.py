import pandas
import plotly.express as px


def bar_chart_by_trophies():
    df = pandas.read_csv('BrawlStars.csv')
    fig = px.bar(df, x="Name", y="Trophies", title="Hero Ranked by trophies",
                 hover_data=['Ranks'], color="Trophies")
    fig.show()  # for debug
    return fig


def bar_chart_by_hero_parity():
    df = pandas.read_csv('BrawlStars.csv')
    fig = px.bar(df, x="Hero Rarity", y="Trophies", title="Hero by Parity in bar",
                 barmode='group', color="Trophies", hover_data=['Ranks', 'Name'])
    # fig.show() # for debug
    return fig


def bar_chart_by_hero_class():
    df = pandas.read_csv('BrawlStars.csv')
    fig = px.bar(df, x="Hero Class", y="Trophies", title="Hero by Class in bar",
                 barmode='group', color="Trophies", hover_data=['Ranks', 'Name'])
    # fig.show() # for debug
    return fig

