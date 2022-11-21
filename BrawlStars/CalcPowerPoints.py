from BrawlStarData import *


def required_power_points(hero_list, final_hero_list):
    total_required = 0
    for hero in hero_list:
        hero_required = 0
        for level_value in HERO_UPGRADE_REQUIRED:
            if hero[1] <= level_value[0]:
                hero_required += level_value[1]
            else:
                pass
        actual_required = hero_required - hero[2]
        total_required += actual_required
        print(hero[0] + " still required power points ---> " + str(actual_required))
        # hero_temp = {"name": hero[0], "required power points": actual_required}
        # final_hero_list.append(hero_temp)
        final_hero_list.append({"Name": hero[0], "required power points": actual_required})

    print("\nYou still require power points is " + str(total_required))
    print(final_hero_list)


def sort_heroes(hero_list, sort_element_first=0, sort_element_second=0, sort_element_third=0):
    # name is the first element in hero parameter tuple
    hero_num = len(hero_list)
    for i in range(0, hero_num - 1):
        for j in range(i + 1, hero_num):
            if hero_list[i][sort_element_first] > hero_list[j][sort_element_first]:
                temp_hero = hero_list[i]
                hero_list[i] = hero_list[j]
                hero_list[j] = temp_hero
            elif hero_list[i][sort_element_first] == hero_list[j][sort_element_first]:
                # if the compared element are equal, then sort by the second element
                if hero_list[i][sort_element_second] > hero_list[j][sort_element_second]:
                    temp_hero = hero_list[i]
                    hero_list[i] = hero_list[j]
                    hero_list[j] = temp_hero
            else:
                pass
    print("Sort the heroes by " + HERO_PARAS[sort_element_first])
    print(hero_list)


if __name__ == '__main__':
    # required_power_points(TRAVIS_HERO_LIST, TRAVIS_HERO_FINAL)
    sort_heroes(TRAVIS_HERO_LIST, 0, 0)
