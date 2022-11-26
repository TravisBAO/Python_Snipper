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

HERO_TYPE = ("STARTING BRAWLER", "TROPHY ROAD REWARD", "RARE", "SUPER RARE", "EPIC", "MYTHIC", "LEGENDARY", "CHROMATIC")
FIGHT_TYPE = ("DAMAGE DEALER", "TANK", )
HERO_PARAS = ("Name", "Trophies", "Power Level", "Power Points", "Rank", "Hero Type", "Fight Type", "Gadget",
              "Star Power", "Gear")

# hero list is a list of data type "HERO_PARAS"
TRAVIS_HERO_LIST = [
    ('SHELLY', 800, 11, 0, 26, 'STARTING BRAWLER', 'DAMAGE DEALER'),
    ('EMZ', 740, 11, 0, 24, 'TROPHY ROAD REWARD', 'DAMAGE DEALER'),
    ('BULL', 715, 10, 648, 25, 'TROPHY ROAD REWARD', 'TANK'),
    ('PENNY', 703, 10, 465, 24),
    ('EDGAR', 702, 11, 0, 23, 'EPIC'),
    ('JACKY', 678, 10, 887, 25),
    ('LEON', 657, 9, 1224, 23),
    ('SPIKE', 652, 10, 281, 22),
    ('BELLE', 637, 11, 0, 23, 'CHROMATIC'),
    ('GALE', 632, 10, 207, 22),
    ('AMBER', 629, 9, 423, 22),
    ('BEE', 622, 11, 0, 23, 'EPIC'),
    ('COLETTE', 608, 9, 975, 22),
    ('RUFFS', 601, 9, 1092, 22),
    ('JESSIE', 601, 9, 1013, 22),
    ('NITA', 599, 9, 1116, 22),
    ('MR.P', 599, 9, 716, 22),
    ('8-BIT', 599, 9, 1136, 23),
    ('BIBI', 590, 9, 1037, 22),
    ('BO', 585, 9, 1055, 22),
    ('MAX', 582, 9, 1074, 22),
    ('CROW', 579, 9, 315, 22),
    ('GRIFF', 567, 10, 87, 21),
    ('EL PRIMO', 564, 9, 1272, 23),
    ('SURGE', 563, 9, 839, 23),
    ('BUSTER', 562, 9, 28, 21),
    ('PAM', 557, 9, 990, 21),
    ('LOU', 555, 9, 1223, 22),
    ('STU', 552, 10, 361, 21),
    ('FANG', 549, 9, 182, 21),
    ('MORTIS', 545, 10, 137, 20),
    ('ROSA', 536, 9, 901, 21),
    ('LOLA', 530, 9, 144, 21),
    ('DYNAMIKE', 525, 9, 1030, 20),
    ('TICK', 522, 9, 998, 21),
    ('DARRYL', 518, 8, 1361, 22),
    ('BYRON', 512, 9, 960, 21),
    ('BARLEY', 508, 7, 1937, 21),
    ('POCO', 506, 7, 1603, 20),
    ('BONNIE', 506, 8, 399, 20),
    ('SQUEAK', 505, 8, 131, 20),
    ('SPROUT', 505, 8, 1481, 20),
    ('BUZZ', 505, 8, 629, 20),
    ('TARA', 503, 8, 1167, 20),
    ('GUS', 501, 9, 84, 20),
    ('RICO', 500, 9, 1007, 22),
    ('PIPER', 500, 7, 1823, 20),
    ('JANET', 500, 8, 385, 20),
    ('GENE', 500, 7, 759, 20),
    ('FRANK', 500, 9, 926, 21),
    ('COLT', 500, 7, 1829, 20),
    ('CARL', 500, 7, 1911, 20),
    ('BROCK', 500, 8, 1415, 21),
    ('ASH', 500, 8, 733, 21),
    ('NANI', 499, 8, 1543, 20),
    ('EVE', 473, 8, 270, 18),
    ('GROM', 463, 7, 477, 19),
    ('SAM', 423, 7, 208, 16),
    ('OTIS', 422, 8, 328, 18),
    ('MEG', 385, 8, 69, 17),
    ('SANDY', 0, 0, 0, 0)
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
