#!/usr/bin/python3
def max_integer(my_list=[]):
    i = len(my_list) - 1
    new_list = my_list.copy()

    if new_list:
        while i > 1:
            j = 0

            while j < i:
                if new_list[j] > new_list[j + 1]:
                    temp = new_list[j]
                    new_list[j] = new_list[j + 1]
                    new_list[j + 1] = temp

                j += 1

            i -= 1

        return new_list[-1]
    return None
