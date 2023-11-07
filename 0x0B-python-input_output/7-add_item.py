#!/usr/bin/python3
import sys
from os.path import exists
from 5-save_to_json_file import save_to_json_file
from 6-load_from_json_file import load_from_json_file


def add_item():
    # Check if the add_item.json file exists
    if exists("add_item.json"):
        # Load the existing list from the file
        my_list = load_from_json_file("add_item.json")
    else:
        # If the file doesn't exist, create an empty list
        my_list = []

    # Add command-line arguments to the list
    for arg in sys.argv[1:]:
        my_list.append(arg)

    # Save the updated list to add_item.json
    save_to_json_file(my_list, "add_item.json")
