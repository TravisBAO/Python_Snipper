from BrawlStarData import *


def required_power_points(hero_list, final_hero_list):
    total_required = 0
    for hero in hero_list:
        hero_required = 0
        for level_value in HERO_POWER_LEVEL_UPGRADE_REQUIRED:
            if hero[2] <= level_value[0]:  # hero[2] is current power level, level_value[0] is level number
                hero_required += level_value[1]  # level_value[1] is required power points to upgrade to next level
            else:
                pass
        actual_required = hero_required - hero[3]  # hero[3] is current power points
        total_required += actual_required
        print(hero[0] + " still required power points ---> " + str(actual_required))
        # hero_temp = {"name": hero[0], "required power points": actual_required}
        # final_hero_list.append(hero_temp)
        final_hero_list.append({"Name": hero[0], "requires power points": actual_required})

    print("\nYou still require power points is " + str(total_required))
    print(final_hero_list)


if __name__ == '__main__':
    required_power_points(TRAVIS_HERO_LIST, TRAVIS_HERO_FINAL)
