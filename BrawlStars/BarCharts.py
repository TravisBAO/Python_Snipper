import pandas
import plotly.express as px

from BrawlStars.BrawlStarData import import_data_to_csv


def bar_chart_by_trophies():
    df = pandas.read_csv('BrawlStars.csv')
    fig = px.bar(df, x="Name", y="Trophies", title="Hero's Trophies",
                 hover_data=['Rank'], color="Trophies")
    fig.show()


if __name__ == "__main__":
    import_data_to_csv()
    bar_chart_by_trophies()

