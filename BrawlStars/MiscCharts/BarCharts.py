import pandas
import plotly.express as px

from BrawlStars.Datas.BrawlStarData import import_data_to_csv


def bar_chart_by_trophies():
    df = pandas.read_csv('BrawlStars.csv')
    fig = px.bar(df, x="Name", y="Trophies", title="Hero's Trophies",
                 hover_data=['Rank'], color="Trophies")
    fig.show()  # for debug
    return fig


def bar_chart_by_hero_parity():
    df = pandas.read_csv('BrawlStars.csv')
    fig = px.bar(df, x="Hero Rarity", y="Trophies", title="Hero's Trophies", barmode='group', color="Trophies",
                 hover_data=['Rank', 'Name'])
    # fig.show() # for debug
    return fig


def bar_chart_by_hero_class():
    df = pandas.read_csv('BrawlStars.csv')
    fig = px.bar(df, x="Hero Class", y="Trophies", title="Hero's Trophies", barmode='group',
                 color="Trophies", hover_data=['Rank', 'Name'])
    # fig.show() # for debug
    return fig


def histogram_chart_by_hero_parity():
    df = pandas.read_csv('BrawlStars.csv')
    fig = px.histogram(df, x="Hero Rarity", y="Trophies", title="Hero's Trophies", barmode='group',
                       color="Trophies")
    # fig.show() # for debug
    return fig


def histogram_chart_by_hero_class():
    df = pandas.read_csv('BrawlStars.csv')
    fig = px.histogram(df, x="Hero Class", y="Trophies", title="Hero's Trophies", barmode='group',
                       color="Trophies", histfunc='max')
    # fig.show() # for debug
    return fig


def charts_collection():
    with open('graph.html', 'a') as charts:
        # include_plotlyjs='cdn' only in the first figure and include_plotlyjs=False in subsequent.
        # No need to load javascript multiple times
        charts.write(bar_chart_by_trophies().to_html(full_html=False, include_plotlyjs='cdn'))
        charts.write(bar_chart_by_hero_parity().to_html(full_html=False, include_plotlyjs='cdn'))


if __name__ == "__main__":
    # import_data_to_csv()
    import_data_to_csv("brawlstars", "hero_historical_data")

    bar_chart_by_trophies()
    # bar_chart_by_hero_parity()
    # bar_chart_by_hero_class()
    # histogram_chart_by_hero_class()
    # histogram_chart_by_hero_parity()

    # charts_collection()

