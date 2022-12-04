from BrawlStars.Datas.BrawlStarData import HERO_RANKs, TRAVIS_HERO_LIST


def up_to_level(level=20):
    """
    To calculate the trophies when all stars reach the dedicated level
    @param level:
    """
    level_trophy = 0
    trophies_increment = 0
    final_trophies_with_required_level = 0
    current_total_trophies = 0
    for each_level in HERO_RANKs:
        if level == each_level[0]:
            level_trophy = each_level[1]
            break
    for each_star in TRAVIS_HERO_LIST:
        if each_star[1] < level_trophy:
            potential_trophies = level_trophy - each_star[1]
            trophies_increment += potential_trophies
            print(each_star[0] + " still misses " + str(potential_trophies) + " trophies for level " + str(level))
        else:
            print(each_star[0] + " has reached level " + str(level))
        current_total_trophies += each_star[1]
    final_trophies_with_required_level = current_total_trophies + trophies_increment
    print('\n')
    print('The current trophies is ' + str(current_total_trophies))
    print("It'll increase " + str(trophies_increment) +
          " trophies when all stars reach level " + str(level))
    print("And the final total trophies is "
          + str(final_trophies_with_required_level))
    return trophies_increment, final_trophies_with_required_level


def up_to_trophies(trophy=500):
    """
    To calculate the trophies when all stars reach the dedicated trophy
    @param trophy: default= 500, and value would be the level line 524, 549, 574, 599
    @return:
    """
    trophies_increment = 0
    final_trophies_with_dedicated_trophy = 0
    current_total_trophies = 0

    for each_star in TRAVIS_HERO_LIST:
        if each_star[1] < trophy:
            potential_trophies = trophy - each_star[1]
            trophies_increment += potential_trophies
            print(each_star[0] + " still misses " + str(potential_trophies) + " trophies for " + str(trophy))
        else:
            print(each_star[0] + " has reached trophy " + str(trophy))
        current_total_trophies += each_star[1]
    final_trophies_with_dedicated_trophy = current_total_trophies + trophies_increment
    print('\n')
    print('The current trophies is ' + str(current_total_trophies))
    print("It'll increase " + str(trophies_increment) +
          " trophies when all stars reach trophy " + str(trophy))
    print("And the final total trophies is "
          + str(final_trophies_with_dedicated_trophy))
    return trophies_increment, final_trophies_with_dedicated_trophy


if __name__ == "__main__":
    # up_to_level(21)
    up_to_trophies(524)
