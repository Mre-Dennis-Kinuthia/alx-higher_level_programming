#!/usr/bin/python3

def element_at(my_list, idx):
    if idx < 0 and idx >= len(my_list):
        return None
    else:
        for i in range(0, len(my_list)):
            print("element at index {:d} is {}".format(idx, my_list[idx]))
