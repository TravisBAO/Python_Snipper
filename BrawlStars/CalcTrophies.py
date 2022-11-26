from BrawlStarData import *


def up_to_level(level=20):
    """
    To calculate the trophies when all stars reach the dedicated level
    @param level:
    """
    level_trophy = 0
    trophies_total_with_required_level = 0
    for each_level in HERO_RANKs:
        if level == each_level[0]:
            level_trophy = each_level[1]
            break
    for each_star in TRAVIS_HERO_LIST:
        if each_star[1] < level_trophy:
            potential_trophies = level_trophy - each_star[1]
            trophies_total_with_required_level += potential_trophies
            print(each_star[0] + " still misses " + str(potential_trophies) + " trophies for level " + str(level))
        else:
            print(each_star[0] + " has reached level " + str(level))
    print("\nIt'll increase " + str(trophies_total_with_required_level) +
          " trophies when all stars reach level " + str(level))


if __name__ == "__main__":
    up_to_level(20)
