from BrawlStars.Datas.BrawlStarData import HERO_RANKS, TRAVIS_HERO_LIST


def up_to_level(level=20):
    """
    To calculate the trophies when all stars reach the dedicated level
    @param level:
    """
    level_trophy = 0
    trophies_increment = 0
    final_trophies_with_required_level = 0
    current_total_trophies = 0
    for each_level in HERO_RANKS:
        if level == each_level[0]:
            level_trophy = each_level[1]
            break
    for each_star in TRAVIS_HERO_LIST:
        if each_star[1] < level_trophy:
            potential_trophies = level_trophy - each_star[1]
            trophies_increment += potential_trophies
            print(each_star[0] + "'s current trophy is " + str(each_star[1])
                  + ", and increases " + str(potential_trophies) + " to level " + str(level))
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
            print(each_star[0] + "'s current trophy is " + str(each_star[1])
                  + ", and increases " + str(potential_trophies) + " trophies to " + str(trophy))
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


def season_end_decrement():
    trophy_decrement = 0
    current_total_trophies = 0

    final_trophies = 0

    for each_star in TRAVIS_HERO_LIST:
        hero_final_trophy = 0
        temp_decrement = 0
        trophy_point = 500

        current_total_trophies += each_star[1]

        while each_star[1] >= trophy_point:
            trophy_point += 25
        if trophy_point == 500:
            hero_final_trophy = each_star[1]
        elif trophy_point == 525:
            hero_final_trophy = 500
        else:
            hero_final_trophy = trophy_point - 25 - 1

        temp_decrement = each_star[1] - hero_final_trophy
        trophy_decrement += temp_decrement
        final_trophies += hero_final_trophy

        if temp_decrement != 0:
            print(each_star[0] + " decreases " + str(temp_decrement) +
                  ": from " + str(each_star[1]) + " to " + str(hero_final_trophy))
        else:
            print(each_star[0] + " keeps on " + str(each_star[1]))

    print("----------------------------------------------->")
    print("Current trophies is " + str(current_total_trophies))
    print("Will decrease to " + str(final_trophies))
    return trophy_decrement


def to_reach_current_rank():
    trophy_increment = 0
    current_total_trophy = 0
    for each_star in TRAVIS_HERO_LIST:
        # each_star[0]: Name, each_star[1]: trophy, each_star[4]: rank
        hero_increment = 0
        current_total_trophy += each_star[1]
        for each_rank in HERO_RANKS:
            if each_star[4] == each_rank[0]:
                if each_star[1] < each_rank[1]:
                    hero_increment = each_rank[1] - each_star[1]
                    trophy_increment += hero_increment

                    print("-----------------------------------------")
                    print(each_star[0] + " current trophy is " + str(each_star[1]))
                    print(each_star[0] + " maximal trophy is " + str(each_rank[1]))
                else:
                    pass
            else:
                pass
    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
    print("Current total trophy is " + str(current_total_trophy))
    print("Total trophy will increase " + str(trophy_increment)
          + " and reach " + str(current_total_trophy + trophy_increment))
    return trophy_increment


if __name__ == "__main__":
    # up_to_level(21)
    # up_to_trophies(550)
    # season_end_decrement()
    to_reach_current_rank()
