#!/usr/bin/python3
"""Adds all arguments to a python list and saves them to a file"""

import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

args = sys.argv[1:]
filename = "add_item.json"

try:
    deserial_list = load_from_json_file(filename)
except FileNotFoundError:
    deserial_list = []

save_to_json_file(deserial_list + args, filename)
