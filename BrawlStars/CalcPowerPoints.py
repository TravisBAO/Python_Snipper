from BrawlStarData import *
from BrawlStars.Utils import sort_ascending, sort_descending


def required_power_points(hero_list, final_hero_list):
    total_required = 0
    for hero in hero_list:
        hero_required = 0
        for level_value in HERO_UPGRADE_REQUIRED:
            if hero[2] <= level_value[0]:  # hero[2] is current power level, level_value[0] is level number
                hero_required += level_value[1]  # level_value[1] is required power points to upgrade to next level
            else:
                pass
        actual_required = hero_required - hero[3]  # hero[3] is current power points
        total_required += actual_required
        print(hero[0] + " still required power points ---> " + str(actual_required))
        # hero_temp = {"name": hero[0], "required power points": actual_required}
        # final_hero_list.append(hero_temp)
        final_hero_list.append({"Name": hero[0], "required power points": actual_required})

    print("\nYou still require power points is " + str(total_required))
    print(final_hero_list)


def sort_heroes(hero_list, rank_type="Descending", sort_element_first=0, sort_element_second=0, sort_element_third=0):
    # name is the first element in hero parameter tuple
    hero_num = len(hero_list)
    for i in range(0, hero_num - 1):
        for j in range(i + 1, hero_num):
            if rank_type == "Ascending":
                hero_list[i], hero_list[j] = sort_ascending(hero_list[i], hero_list[j], sort_element_first,
                                                            sort_element_second)
            elif rank_type == "Descending":
                hero_list[i], hero_list[j] = sort_descending(hero_list[i], hero_list[j], sort_element_first,
                                                             sort_element_second)
            else:
                print("rank should be 'Ascending' or 'Descending'")

    print("Sort the heroes by " + HERO_PARAS[sort_element_first])
    # print heroes by lines
    for each_hero in hero_list:
        print(str(each_hero) + ',')


if __name__ == '__main__':
    # required_power_points(TRAVIS_HERO_LIST, TRAVIS_HERO_FINAL)
    sort_heroes(TRAVIS_HERO_LIST, rank_type="Descending", sort_element_first=1, sort_element_second=0)
