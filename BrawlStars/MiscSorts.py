from BrawlStarData import *
from BrawlStars.Utils import sort_ascending, sort_descending


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
    sort_heroes(TRAVIS_HERO_LIST, rank_type="Descending", sort_element_first=1, sort_element_second=0)