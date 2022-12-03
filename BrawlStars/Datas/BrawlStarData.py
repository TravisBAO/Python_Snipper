# database tables
db_table_TRAVIS_HERO_LIST = ("Name", "Hero_Rarity", "Hero_Class")
db_table_hero_historical_data = ("Name", "Trophies", "Power_Level", "Power_Points", "Ranks", "Date")


# Structure: (level, upgrade required power points, upgrade required Coins)
HERO_POWER_LEVEL_UPGRADE_REQUIRED = [
    (0, 0, 0),
    (1, 20, 20),
    (2, 30, 35),
    (3, 50, 75),
    (4, 80, 140),
    (5, 130, 290),
    (6, 210, 480),
    (7, 340, 800),
    (8, 550, 1250),
    (9, 890, 1875),
    (10, 1440, 2800)
]
# Structure: (rank, trophy required)
HERO_RANKs = [
    (20, 500),
    (21, 550),
    (22, 600),
    (23, 650),
    (24, 700),
    (25, 750),
    (26, 800),
    (27, 850),
]

HERO_RARITY = ("STARTING BRAWLER", "TROPHY ROAD REWARD", "RARE", "SUPER RARE",
               "EPIC", "MYTHIC", "LEGENDARY", "CHROMATIC")
HERO_CLASS = ("DAMAGE DEALER", "TANK", "HYBRID", "ASSASSIN", "SUPPORT")
HERO_PARAS = ("Name",
              "Trophies",
              "Power Level",
              "Power Points",
              "Rank",
              "Hero Rarity",
              "Hero Class",
              "Gadget", "Star Power", "Gear")

# hero list is a list of data type "HERO_PARAS"
TRAVIS_HERO_LIST = [
    ('SHELLY', 800, 11, 0, 26, 'STARTING BRAWLER', 'DAMAGE DEALER'),
    ('EMZ', 740, 11, 0, 24, 'TROPHY ROAD REWARD', 'DAMAGE DEALER'),
    ('PENNY', 703, 10, 551, 24, 'SUPER RARE', 'DAMAGE DEALER'),
    ('EDGAR', 701, 11, 0, 24, 'EPIC', 'ASSASSIN'),
    ('JACKY', 700, 10, 1440, 25, 'SUPER RARE', 'TANK'),
    ('BULL', 700, 10, 671, 25, 'TROPHY ROAD REWARD', 'TANK'),
    ('LEON', 657, 9, 1244, 23, 'LEGENDARY', 'ASSASSIN'),
    ('BELLE', 656, 11, 0, 23, 'CHROMATIC', 'DAMAGE DEALER'),
    ('CROW', 651, 9, 359, 23, 'LEGENDARY', 'ASSASSIN'),
    ('SPIKE', 650, 10, 281, 23, 'LEGENDARY', 'DAMAGE DEALER'),
    ('GALE', 632, 10, 257, 22, 'CHROMATIC', 'HYBRID'),
    ('AMBER', 629, 9, 423, 22, 'LEGENDARY', 'DAMAGE DEALER'),
    ('COLETTE', 608, 9, 1024, 22, 'CHROMATIC', 'DAMAGE DEALER'),
    ('BUZZ', 608, 9, 79, 22, 'CHROMATIC', 'ASSASSIN'),
    ('BUSTER', 605, 9, 28, 22, 'CHROMATIC', 'TANK'),
    ('GRIFF', 604, 10, 128, 22, 'EPIC', 'DAMAGE DEALER'),
    ('RUFFS', 601, 10, 1092, 22, 'CHROMATIC', 'SUPPORT'),
    ('NITA', 601, 9, 1136, 22, 'TROPHY ROAD REWARD', 'DAMAGE DEALER'),
    ('MR.P', 601, 9, 890, 22, 'MYTHIC', 'DAMAGE DEALER'),
    ('JESSIE', 601, 9, 1013, 22, 'TROPHY ROAD REWARD', 'DAMAGE DEALER'),
    ('BO', 601, 9, 1070, 22, 'TROPHY ROAD REWARD', 'DAMAGE DEALER'),
    ('ASH', 601, 9, 217, 22, 'CHROMATIC', 'TANK'),
    ('BIBI', 590, 9, 1057, 22, 'EPIC', 'DAMAGE DEALER'),
    ('8-BIT', 581, 9, 1144, 23, 'TROPHY ROAD REWARD', 'DAMAGE DEALER'),
    ('STU', 576, 10, 385, 21, 'TROPHY ROAD REWARD', 'ASSASSIN'),
    ('BEE', 569, 11, 0, 23, 'EPIC', 'DAMAGE DEALER'),
    ('EL PRIMO', 564, 9, 1286, 23, 'RARE', 'TANK'),
    ('SURGE', 563, 9, 916, 23, 'CHROMATIC', 'DAMAGE DEALER'),
    ('PAM', 557, 9, 990, 21, 'EPIC', 'SUPPORT'),
    ('LOU', 555, 9, 1223, 22, 'CHROMATIC', 'HYBRID'),
    ('ROSA', 552, 9, 931, 21, 'RARE', 'TANK'),
    ('MAX', 551, 9, 1074, 22, 'MYTHIC', 'SUPPORT'),
    ('MORTIS', 546, 10, 191, 21, 'MYTHIC', 'ASSASSIN'),
    ('FANG', 533, 9, 191, 21, 'CHROMATIC', 'DAMAGE DEALER'),
    ('GUS', 532, 9, 148, 20, 'SUPER RARE', 'SUPPORT'),
    ('TICK', 529, 9, 998, 21, 'TROPHY ROAD REWARD', 'DAMAGE DEALER'),
    ('DYNAMIKE', 525, 9, 1030, 20, 'TROPHY ROAD REWARD', 'DAMAGE DEALER'),
    ('BROCK', 519, 8, 1415, 21, 'TROPHY ROAD REWARD', 'DAMAGE DEALER'),
    ('DARRYL', 518, 8, 1361, 22, 'SUPER RARE', 'HYBRID'),
    ('EVE', 510, 8, 270, 20, 'CHROMATIC', 'DAMAGE DEALER'),
    ('BYRON', 510, 9, 960, 21, 'MYTHIC', 'SUPPORT'),
    ('POCO', 508, 7, 1615, 20, 'RARE', 'SUPPORT'),
    ('JANET', 508, 8, 610, 20, 'CHROMATIC', 'DAMAGE DEALER'),
    ('BONNIE', 508, 8, 610, 20, 'EPIC', 'HYBRID'),
    ('SQUEAK', 505, 8, 167, 20, 'MYTHIC', 'DAMAGE DEALER'),
    ('NANI', 505, 8, 1543, 20, 'EPIC', 'DAMAGE DEALER'),
    ('LOLA', 505, 9, 186, 21, 'CHROMATIC', 'DAMAGE DEALER'),
    ('TARA', 503, 8, 1167, 20, 'MYTHIC', 'DAMAGE DEALER'),
    ('BARLEY', 502, 7, 1937, 21, 'RARE', 'DAMAGE DEALER'),
    ('RICO', 500, 9, 1007, 22, 'SUPER RARE', 'DAMAGE DEALER'),
    ('PIPER', 500, 7, 1823, 20, 'EPIC', 'DAMAGE DEALER'),
    ('FRANK', 500, 9, 926, 21, 'EPIC', 'TANK'),
    ('COLT', 500, 7, 1829, 20, 'TROPHY ROAD REWARD', 'DAMAGE DEALER'),
    ('CARL', 500, 7, 1911, 20, 'SUPER RARE', 'DAMAGE DEALER'),
    ('SPROUT', 499, 8, 1496, 20, 'MYTHIC', 'SUPPORT'),
    ('GENE', 498, 7, 759, 20, 'MYTHIC', 'SUPPORT'),
    ('GROM', 463, 7, 477, 19, 'EPIC', 'DAMAGE DEALER'),
    ('SAM', 423, 7, 208, 18, 'CHROMATIC', 'DAMAGE DEALER'),
    ('OTIS', 422, 8, 328, 18, 'CHROMATIC', 'DAMAGE DEALER'),
    ('MEG', 406, 8, 118, 17, 'LEGENDARY', 'DAMAGE DEALER'),
    ('SANDY', 0, 0, 0, 0, 'LEGENDARY', 'SUPPORT')
]
# {"name" : "string", "required power points": uint, "required coins" : uint}
TRAVIS_HERO_FINAL = []




#
# if __name__ == '__main__':

    # insert data to tables
    # insert_data_to_database("brawlstars", "travis_hero_list")
    # insert_data_to_database("brawlstars", "hero_historical_data")

    # update data to tables
    # update_data_to_database("brawlstars", "travis_hero_list")
    # update_data_to_database("brawlstars", "hero_historical_data")

    # import_data_to_csv("brawlstars", "hero_historical_data")
