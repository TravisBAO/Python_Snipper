

def sort_descending(sort_target_one, sort_target_two, sort_element_first, sort_element_second=0):
    if sort_target_one[sort_element_first] < sort_target_two[sort_element_first]:
        temp_hero = sort_target_one
        sort_target_one = sort_target_two
        sort_target_two = temp_hero
    elif sort_target_one[sort_element_first] == sort_target_two[sort_element_first]:
        if sort_target_one[sort_element_second] < sort_target_two[sort_element_second]:
            temp_hero = sort_target_one
            sort_target_one = sort_target_two
            sort_target_two = temp_hero
    else:
        pass
    return sort_target_one, sort_target_two


def sort_ascending(sort_target_one, sort_target_two, sort_element_first, sort_element_second=0):
    if sort_target_one[sort_element_first] > sort_target_two[sort_element_first]:
        temp_hero = sort_target_one
        sort_target_one = sort_target_two
        sort_target_two = temp_hero
    elif sort_target_one[sort_element_first] == sort_target_two[sort_element_first]:
        if sort_target_one[sort_element_second] > sort_target_two[sort_element_second]:
            temp_hero = sort_target_one
            sort_target_one = sort_target_two
            sort_target_two = temp_hero
    else:
        pass
    return sort_target_one, sort_target_two
