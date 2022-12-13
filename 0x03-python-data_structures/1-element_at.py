#!/usr/bin/python3

def element_at(my_list, idx):
    if idx < 0 and idx >= len(my_list):
        return None
    else:
        print("element at index {:d} is {}".format(idx, my_list[idx]))
