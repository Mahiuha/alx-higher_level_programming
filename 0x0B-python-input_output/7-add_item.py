#!/usr/bin/python3
""" Load, add, save  """
from sys import argv


load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

""" Script that adds all arguments to a Python list,
and then save them to a file """
try:
    add_i = load_from_json_file('add_item.json')
    save_to_json_file(add_i + argv[1:], 'add_item.json')
except Exception:
    save_to_json_file(argv[1:], 'add_item.json')
