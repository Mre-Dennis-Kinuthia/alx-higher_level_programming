#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if tuple_a and tuple_b:
        if len(tuple_a) < 2 and len(tuple_b) < 2:
            a = tuple_a[0] + tuple_b[0]
            b = 0
        elif len(tuple_a) < 2:
            a = tuple_a[0] + tuple_b[0]
            b = 0 + tuple_b[1]
        elif len(tuple_b) < 2:
            a = tuple_a[0] + tuple_b[0]
            b = tuple_a[1] + 0
        else:
            a = tuple_a[0] + tuple_b[0]
            b = tuple_a[1] + tuple_b[1]
        tuple_c = (a, b)
        return tuple_c
    else:
        if not tuple_b and not tuple_a:
            tuple_c = (0, 0)
            return tuple_c
        elif not tuple_a:
            return tuple_b
        else:
            return tuple_a
