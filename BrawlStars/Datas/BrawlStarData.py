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
HERO_RANKS = [
    (20, 500),
    (21, 550),
    (22, 600),
    (23, 650),
    (24, 700),
    (25, 750),
    (26, 800),
    (27, 850),
    (28, 900)
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
    ('SHELLY', 779, 11, 0, 26, 'STARTING BRAWLER', 'DAMAGE DEALER'),
    ('PENNY', 704, 10, 551, 24, 'SUPER RARE', 'DAMAGE DEALER'),
    ('EMZ', 703, 11, 0, 24, 'TROPHY ROAD REWARD', 'DAMAGE DEALER'),
    ('EDGAR', 701, 11, 0, 24, 'EPIC', 'ASSASSIN'),
    ('JACKY', 700, 10, 1440, 25, 'SUPER RARE', 'TANK'),
    ('BULL', 700, 10, 727, 25, 'TROPHY ROAD REWARD', 'TANK'),
    ('SPIKE', 676, 10, 281, 23, 'LEGENDARY', 'DAMAGE DEALER'),
    ('BELLE', 664, 11, 0, 23, 'CHROMATIC', 'DAMAGE DEALER'),
    ('BUZZ', 659, 9, 79, 22, 'CHROMATIC', 'ASSASSIN'),
    ('LEON', 657, 9, 1279, 23, 'LEGENDARY', 'ASSASSIN'),
    ('CROW', 652, 9, 359, 23, 'LEGENDARY', 'ASSASSIN'),
    ('GALE', 632, 10, 257, 22, 'CHROMATIC', 'HYBRID'),
    ('AMBER', 629, 9, 423, 22, 'LEGENDARY', 'DAMAGE DEALER'),
    ('COLETTE', 608, 9, 1024, 22, 'CHROMATIC', 'DAMAGE DEALER'),
    ('BEE', 605, 11, 0, 23, 'EPIC', 'DAMAGE DEALER'),
    ('RUFFS', 601, 10, 1106, 22, 'CHROMATIC', 'SUPPORT'),
    ('NITA', 601, 9, 1136, 22, 'TROPHY ROAD REWARD', 'DAMAGE DEALER'),
    ('MR.P', 601, 9, 918, 22, 'MYTHIC', 'DAMAGE DEALER'),
    ('JESSIE', 601, 9, 1013, 22, 'TROPHY ROAD REWARD', 'DAMAGE DEALER'),
    ('BO', 601, 10, 195, 22, 'TROPHY ROAD REWARD', 'DAMAGE DEALER'),
    ('BUSTER', 600, 9, 28, 22, 'CHROMATIC', 'TANK'),
    ('BIBI', 590, 9, 1057, 22, 'EPIC', 'DAMAGE DEALER'),
    ('8-BIT', 581, 9, 1156, 23, 'TROPHY ROAD REWARD', 'DAMAGE DEALER'),
    ('ASH', 580, 9, 230, 22, 'CHROMATIC', 'TANK'),
    ('ROSA', 576, 9, 931, 21, 'RARE', 'TANK'),
    ('EL PRIMO', 564, 9, 1286, 23, 'RARE', 'TANK'),
    ('SURGE', 557, 9, 928, 23, 'CHROMATIC', 'DAMAGE DEALER'),
    ('GRIFF', 556, 10, 128, 22, 'EPIC', 'DAMAGE DEALER'),
    ('LOU', 555, 9, 1306, 22, 'CHROMATIC', 'HYBRID'),
    ('DARRYL', 552, 8, 1407, 22, 'SUPER RARE', 'HYBRID'),
    ('FANG', 551, 9, 191, 21, 'CHROMATIC', 'DAMAGE DEALER'),
    ('STU', 550, 10, 404, 21, 'TROPHY ROAD REWARD', 'ASSASSIN'),
    ('PAM', 550, 9, 1001, 21, 'EPIC', 'SUPPORT'),
    ('MORTIS', 550, 10, 191, 21, 'MYTHIC', 'ASSASSIN'),
    ('MAX', 533, 9, 1137, 22, 'MYTHIC', 'SUPPORT'),
    ('GUS', 530, 9, 156, 20, 'SUPER RARE', 'SUPPORT'),
    ('TICK', 528, 9, 998, 21, 'TROPHY ROAD REWARD', 'DAMAGE DEALER'),
    ('SQUEAK', 528, 8, 167, 20, 'MYTHIC', 'DAMAGE DEALER'),
    ('RICO', 528, 9, 1019, 22, 'SUPER RARE', 'DAMAGE DEALER'),
    ('LOLA', 528, 9, 186, 21, 'CHROMATIC', 'DAMAGE DEALER'),
    ('EVE', 528, 8, 286, 20, 'CHROMATIC', 'DAMAGE DEALER'),
    ('OTIS', 527, 9, 118, 20, 'CHROMATIC', 'DAMAGE DEALER'),
    ('JANET', 526, 8, 698, 20, 'CHROMATIC', 'DAMAGE DEALER'),
    ('BYRON', 526, 9, 1016, 21, 'MYTHIC', 'SUPPORT'),
    ('DYNAMIKE', 525, 9, 1050, 20, 'TROPHY ROAD REWARD', 'DAMAGE DEALER'),
    ('FRANK', 516, 9, 926, 21, 'EPIC', 'TANK'),
    ('BROCK', 510, 8, 1424, 21, 'TROPHY ROAD REWARD', 'DAMAGE DEALER'),
    ('POCO', 508, 7, 1615, 20, 'RARE', 'SUPPORT'),
    ('SPROUT', 507, 8, 1496, 20, 'MYTHIC', 'SUPPORT'),
    ('NANI', 505, 8, 1551, 20, 'EPIC', 'DAMAGE DEALER'),
    ('TARA', 503, 8, 1167, 20, 'MYTHIC', 'DAMAGE DEALER'),
    ('GENE', 503, 7, 759, 20, 'MYTHIC', 'SUPPORT'),
    ('BONNIE', 502, 8, 651, 20, 'EPIC', 'HYBRID'),
    ('BARLEY', 502, 7, 1937, 21, 'RARE', 'DAMAGE DEALER'),
    ('PIPER', 500, 7, 1823, 20, 'EPIC', 'DAMAGE DEALER'),
    ('COLT', 500, 7, 1829, 20, 'TROPHY ROAD REWARD', 'DAMAGE DEALER'),
    ('CARL', 500, 7, 1911, 20, 'SUPER RARE', 'DAMAGE DEALER'),
    ('GROM', 477, 7, 477, 19, 'EPIC', 'DAMAGE DEALER'),
    ('SAM', 439, 7, 208, 18, 'CHROMATIC', 'DAMAGE DEALER'),
    ('MEG', 411, 8, 118, 17, 'LEGENDARY', 'DAMAGE DEALER'),
    ('SANDY', 0, 0, 0, 0, 'LEGENDARY', 'SUPPORT')

]
# {"name" : "string", "required power points": uint, "required coins" : uint}
TRAVIS_HERO_FINAL = []
