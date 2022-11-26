import csv
import os.path


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
HERO_PARAS = ("Name", "Trophies", "Power Level", "Power Points", "Rank", "Hero Rarity", "Hero Class", "Gadget",
              "Star Power", "Gear")

# hero list is a list of data type "HERO_PARAS"
TRAVIS_HERO_LIST = [
    ('SHELLY', 800, 11, 0, 26, 'STARTING BRAWLER', 'DAMAGE DEALER'),
    ('EMZ', 740, 11, 0, 24, 'TROPHY ROAD REWARD', 'DAMAGE DEALER'),
    ('BULL', 715, 10, 648, 25, 'TROPHY ROAD REWARD', 'TANK'),
    ('PENNY', 703, 10, 465, 24, 'SUPER RARE', 'DAMAGE DEALER'),
    ('EDGAR', 702, 11, 0, 23, 'EPIC', 'ASSASSIN'),
    ('JACKY', 678, 10, 887, 25, 'SUPER RARE', 'TANK'),
    ('LEON', 657, 9, 1224, 23, 'LEGENDARY', 'ASSASSIN'),
    ('SPIKE', 652, 10, 281, 22, 'LEGENDARY', 'DAMAGE DEALER'),
    ('BELLE', 637, 11, 0, 23, 'CHROMATIC', 'DAMAGE DEALER'),
    ('GALE', 632, 10, 207, 22, 'CHROMATIC', 'HYBRID'),
    ('AMBER', 629, 9, 423, 22, 'LEGENDARY', 'DAMAGE DEALER'),
    ('BEE', 622, 11, 0, 23, 'EPIC', 'DAMAGE DEALER'),
    ('COLETTE', 608, 9, 975, 22, 'CHROMATIC', 'DAMAGE DEALER'),
    ('RUFFS', 601, 9, 1092, 22, 'CHROMATIC', 'SUPPORT'),
    ('JESSIE', 601, 9, 1013, 22, 'TROPHY ROAD REWARD', 'DAMAGE DEALER'),
    ('NITA', 599, 9, 1116, 22, 'TROPHY ROAD REWARD', 'DAMAGE DEALER'),
    ('MR.P', 599, 9, 716, 22, 'MYTHIC', 'DAMAGE DEALER'),
    ('8-BIT', 599, 9, 1136, 23, 'TROPHY ROAD REWARD', 'DAMAGE DEALER'),
    ('BIBI', 590, 9, 1037, 22, 'EPIC', 'DAMAGE DEALER'),
    ('BO', 585, 9, 1055, 22, 'TROPHY ROAD REWARD', 'DAMAGE DEALER'),
    ('MAX', 582, 9, 1074, 22, 'MYTHIC', 'SUPPORT'),
    ('CROW', 579, 9, 315, 22, 'LEGENDARY', 'ASSASSIN'),
    ('GRIFF', 567, 10, 87, 21, 'EPIC', 'DAMAGE DEALER'),
    ('EL PRIMO', 564, 9, 1272, 23, 'RARE', 'TANK'),
    ('SURGE', 563, 9, 839, 23, 'CHROMATIC', 'DAMAGE DEALER'),
    ('BUSTER', 562, 9, 28, 21, 'CHROMATIC', 'TANK'),
    ('PAM', 557, 9, 990, 21, 'EPIC', 'SUPPORT'),
    ('LOU', 555, 9, 1223, 22, 'CHROMATIC', 'HYBRID'),
    ('STU', 552, 10, 361, 21, 'TROPHY ROAD REWARD', 'ASSASSIN'),
    ('FANG', 549, 9, 182, 21, 'CHROMATIC', 'DAMAGE DEALER'),
    ('MORTIS', 545, 10, 137, 20, 'MYTHIC', 'ASSASSIN'),
    ('ROSA', 536, 9, 901, 21, 'RARE', 'TANK'),
    ('LOLA', 530, 9, 144, 21, 'CHROMATIC', 'DAMAGE DEALER'),
    ('DYNAMIKE', 525, 9, 1030, 20, 'TROPHY ROAD REWARD', 'DAMAGE DEALER'),
    ('TICK', 522, 9, 998, 21, 'TROPHY ROAD REWARD', 'DAMAGE DEALER'),
    ('DARRYL', 518, 8, 1361, 22, 'SUPER RARE', 'HYBRID'),
    ('BYRON', 512, 9, 960, 21, 'MYTHIC', 'SUPPORT'),
    ('BARLEY', 508, 7, 1937, 21, 'RARE', 'DAMAGE DEALER'),
    ('POCO', 506, 7, 1603, 20, 'RARE', 'SUPPORT'),
    ('BONNIE', 506, 8, 399, 20, 'EPIC', 'HYBRID'),
    ('SQUEAK', 505, 8, 131, 20, 'MYTHIC', 'DAMAGE DEALER'),
    ('SPROUT', 505, 8, 1481, 20, 'MYTHIC', 'SUPPORT'),
    ('BUZZ', 505, 8, 629, 20, 'CHROMATIC', 'ASSASSIN'),
    ('TARA', 503, 8, 1167, 20, 'MYTHIC', 'DAMAGE DEALER'),
    ('GUS', 501, 9, 84, 20, 'SUPER RARE', 'SUPPORT'),
    ('RICO', 500, 9, 1007, 22, 'SUPER RARE', 'DAMAGE DEALER'),
    ('PIPER', 500, 7, 1823, 20, 'EPIC', 'DAMAGE DEALER'),
    ('JANET', 500, 8, 385, 20, 'CHROMATIC', 'DAMAGE DEALER'),
    ('GENE', 500, 7, 759, 20, 'MYTHIC', 'SUPPORT'),
    ('FRANK', 500, 9, 926, 21, 'EPIC', 'TANK'),
    ('COLT', 500, 7, 1829, 20, 'TROPHY ROAD REWARD', 'DAMAGE DEALER'),
    ('CARL', 500, 7, 1911, 20, 'SUPER RARE', 'DAMAGE DEALER'),
    ('BROCK', 500, 8, 1415, 21, 'TROPHY ROAD REWARD', 'DAMAGE DEALER'),
    ('ASH', 500, 8, 733, 21, 'CHROMATIC', 'TANK'),
    ('NANI', 499, 8, 1543, 20, 'EPIC', 'DAMAGE DEALER'),
    ('EVE', 473, 8, 270, 18, 'CHROMATIC', 'DAMAGE DEALER'),
    ('GROM', 463, 7, 477, 19, 'EPIC', 'DAMAGE DEALER'),
    ('SAM', 423, 7, 208, 16, 'CHROMATIC', 'DAMAGE DEALER'),
    ('OTIS', 422, 8, 328, 18, 'CHROMATIC', 'DAMAGE DEALER'),
    ('MEG', 385, 8, 69, 17, 'LEGENDARY', 'DAMAGE DEALER'),
    ('SANDY', 0, 0, 0, 0, 'LEGENDARY', 'SUPPORT')
]
# {"name" : "string", "required power points": uint, "required coins" : uint}
TRAVIS_HERO_FINAL = []


def import_data_to_csv():
    if os.path.exists("BrawlStars.csv"):
        os.remove("BrawlStars.csv")
    with open("BrawlStars.csv", "a") as BrawlStarsFile:
        writer = csv.writer(BrawlStarsFile)
        writer.writerow(HERO_PARAS)
        writer.writerows(TRAVIS_HERO_LIST)
