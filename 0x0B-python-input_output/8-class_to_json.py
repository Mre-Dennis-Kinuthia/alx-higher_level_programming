#!/usr/bin/python3
"""_summary_
"""


def class_to_json(obj):
    """_summary_

    Args:
        obj (_type_): _description_

    Returns:
        _type_: _description_
    """
    json_obj = {}
    for key in obj.__dict__:
        if isinstance(obj.__dict__[key], (int, str, float, bool, list, dict)):
            json_obj[key] = obj.__dict__[key]
    return json_obj
