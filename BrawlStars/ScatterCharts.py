import pandas
import plotly.express as px

from BrawlStars.BrawlStarData import import_data_to_csv


def scatter_chart_by_trophies():
    df = pandas.read_csv('BrawlStars.csv')
    fig = px.scatter(df, x="Power Level", y="Trophies", title="Hero's Trophies",
                     hover_data=['Name', 'Rank'], color="Rank", size="Rank")
    fig.show()


if __name__ == "__main__":
    import_data_to_csv()
    scatter_chart_by_trophies()

