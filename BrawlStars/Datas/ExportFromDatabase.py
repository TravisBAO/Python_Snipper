import csv
import os

from BrawlStars.Datas.BrawlStarData import HERO_PARAS
from BrawlStars.Datas.ImportToDatabase import connect_to_database


def fetch_data_from_database(database, table):
    mydb = connect_to_database(database)
    mycursor = mydb.cursor()
    sql = "SELECT * from" + " " + table
    mycursor.execute(sql)
    return mycursor.fetchall()


if __name__ == '__main__':
    fetch_data_from_database("brawlstars", "hero_historical_data")