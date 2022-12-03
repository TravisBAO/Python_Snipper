import csv
import os.path
import mysql.connector

from datetime import datetime
from BrawlStars.Datas.BrawlStarData import TRAVIS_HERO_LIST


def connect_to_database(database):
    mydb = mysql.connector.connect(
        host="localhost",
        user="Travis",
        password="20030421",
        database=database)
    return mydb


def insert_data_to_database(database, table):
    # connect to database
    mydb = connect_to_database(database)
    mycursor = mydb.cursor()
    if table == "travis_hero_list":
        for each_hero in TRAVIS_HERO_LIST:
            sql = "INSERT INTO " + table + " " + str(db_table_TRAVIS_HERO_LIST).replace("'", "") + " " \
                  + "VALUES (%s, %s, %s)"
            val = (each_hero[0], each_hero[5], each_hero[6])  # Name, Hero_Rarity, Hero_Class
            mycursor.execute(sql, val)
            mydb.commit()
    elif table == "hero_historical_data":
        for each_hero in TRAVIS_HERO_LIST:
            sql = "INSERT INTO " + table + " " + str(db_table_hero_historical_data).replace("'", "") + " " \
                  + "VALUES (%s, %s, %s, %s, %s, %s)"
            val = (each_hero[0], each_hero[1], each_hero[2], each_hero[3], each_hero[4],
                   datetime.now().strftime('%Y-%m-%d')
                   )  # Name,Trophies,Power_Level,Power_Points,Rank,Date
            mycursor.execute(sql, val)
            mydb.commit()
    else:
        pass


def update_data_to_database(database, table):
    """
    This function is to update the dedicated key-value "Unlocked" in table travis_hero_list
    @param database:
    @param table:
    @return:
    """
    # connect to database
    mydb = connect_to_database(database)
    mycursor = mydb.cursor()

    for each_hero in TRAVIS_HERO_LIST:
        sql = "UPDATE" + " " + table + " " + "SET" + " " + "Unlocked" + "=" + "true" \
              + " " + "WHERE" + " " + "Name" + "=" + "(%s)"
        val = (each_hero[0],)
        mycursor.execute(sql, val)
        mydb.commit()
