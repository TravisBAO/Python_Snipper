import csv
import os

from BrawlStars.Datas.BrawlStarData import HERO_PARAS, TRAVIS_HERO_LIST
from BrawlStars.Datas.ExportFromDatabase import fetch_data_from_database


def import_data_to_csv(csv_head, csv_data):
    if os.path.exists("BrawlStars.csv"):
        os.remove("BrawlStars.csv")
    with open("BrawlStars.csv", "a") as BrawlStarsFile:
        writer = csv.writer(BrawlStarsFile)
        writer.writerow(csv_head)
        writer.writerows(csv_data)


if __name__ == '__main__':
    # import_data_to_csv(HERO_PARAS, TRAVIS_HERO_LIST)
    data_from_database = fetch_data_from_database("brawlstars", "hero_historical_data")
    import_data_to_csv(HERO_PARAS, data_from_database)
