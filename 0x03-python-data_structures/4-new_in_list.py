#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    list_copy = my_list.copy()
    if idx < 0 or idx >= len(list_copy):
        return list_copy
    else:
        for i in range(0, len(list_copy)):
            if i == idx:
                list_copy[idx] = element
                return list_copy
