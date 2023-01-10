#!/usr/bin/python3
"""function declaration
"""

import json
import sys
save_to = __import__('5-save_to_json_file').save_to_json_file
load_from = __import__('6-load_from_json_file').load_from_json_file


sys.argv = []
sys.argv = load_from("add_item.json")

n = len(sys.argv)

for i in range(1,n):
    sys.argv.append(i)
save_to(sys.argv, "add_item.json")