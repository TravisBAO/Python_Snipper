import pandas
import plotly.express as px

from BrawlStars.BrawlStarData import import_data_to_csv


def bar_chart_by_trophies():
    df = pandas.read_csv('BrawlStars.csv')
    fig = px.bar(df, x="Name", y="Trophies", title="Hero's Trophies",
                 hover_data=['Rank'], color="Trophies")
    fig.show()


def bar_chart_by_hero_parity():
    df = pandas.read_csv('BrawlStars.csv')
    fig = px.bar(df, x="Hero Rarity", y="Trophies", title="Hero's Trophies", barmode='group', color="Trophies",
                 hover_data=['Rank', 'Name'])
    fig.show()


def bar_chart_by_hero_class():
    df = pandas.read_csv('BrawlStars.csv')
    fig = px.bar(df, x="Hero Class", y="Trophies", title="Hero's Trophies", barmode='group',
                 color="Trophies", hover_data=['Rank', 'Name'])
    fig.show()


def histogram_chart_by_hero_parity():
    df = pandas.read_csv('BrawlStars.csv')
    fig = px.histogram(df, x="Hero Rarity", y="Trophies", title="Hero's Trophies", barmode='group',
                       color="Trophies")
    fig.show()


def histogram_chart_by_hero_class():
    df = pandas.read_csv('BrawlStars.csv')
    fig = px.histogram(df, x="Hero Class", y="Trophies", title="Hero's Trophies", barmode='group',
                       color="Trophies", histfunc='max')
    fig.show()


if __name__ == "__main__":
    import_data_to_csv()

    # bar_chart_by_trophies()
    # bar_chart_by_hero_parity()
    # bar_chart_by_hero_class()

    histogram_chart_by_hero_class()
    # histogram_chart_by_hero_parity()

