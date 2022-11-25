import csv
import os.path
import pandas
import plotly.express as px
from BrawlStars.BrawlStarData import HERO_PARAS, TRAVIS_HERO_LIST


def import_data_to_csv():
    if os.path.exists("BrawlStars.csv"):
        os.remove("BrawlStars.csv")
    with open("BrawlStars.csv", "a") as BrawlStarsFile:
        writer = csv.writer(BrawlStarsFile)
        writer.writerow(HERO_PARAS)
        writer.writerows(TRAVIS_HERO_LIST)


def brawl_stars():
    df = pandas.read_csv('BrawlStars.csv')
    fig = px.scatter(df, x="Power Level", y="Trophies", title="Hero's Trophies",
                     hover_data=['Name', 'Rank'], color="Rank", size="Rank")
    fig.show()


if __name__ == "__main__":
    import_data_to_csv()
    brawl_stars()

