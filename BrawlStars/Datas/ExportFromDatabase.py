from BrawlStars.Datas.BrawlStarData import HERO_PARAS
from BrawlStars.Datas.ImportToDatabase import connect_to_database

# charts required columns lists
bar_chart_trophies = ("Name", "Trophies", "Ranks")

# SQLs
# structure of name: sql_chartType_rankProperty
sql_all = "SELECT * from" + " " + "hero_historical_data"
sql_bar_trophies = "SELECT Name, Trophies, Ranks "\
                   + "FROM hero_historical_data " \
                   + "WHERE Date = (select MAX(Date) " \
                   "FROM hero_historical_data)"


def fetch_data_from_database(database, sql_query):
    mydb = connect_to_database(database)
    mycursor = mydb.cursor()
    mycursor.execute(sql_query)
    return mycursor.fetchall()


if __name__ == '__main__':
    x = fetch_data_from_database("brawlstars", sql_bar_trophies)
    print(x)

