#!/usr/bin/python3
def element_at(my_list, idx):
    if idx < 0 or idx >= len(my_list):
        return None
    else:
        for i in range(0, len(my_list)):
            if i == idx:
                return my_list[idx]
