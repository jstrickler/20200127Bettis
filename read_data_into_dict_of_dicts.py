#!/usr/bin/env python
"""
Knight information service

Reads knights.txt to provide data for King Arthur's knights

But not the knights who say "NI!!"
"""
from pprint import pprint

FILE_NAME = 'DATA/knights.txt'

def main():
    """
    Program entry point

    :return: None
    """
    data = read_data(FILE_NAME)

    pretty(data)
    print()

    print(get_field(data, 'Galahad', 'color'), '\n')

    print_titles(data)

    print_titles()

def read_data(file_name: str) -> dict:
    """
    Read data from the file

    :param file_name: Location of knight data
    :return: knight data as dict of strings
    """
    data = {}

    # file must be in proper format
    with open(file_name) as knights_in:
        for raw_line in knights_in:
            line = raw_line.rstrip()
            name, title, color, quest, comment = line.split(':')
            data[name] = {
                "title": title,
                "color": color,
                "quest": quest,
                "comment": comment,
            }
    return data

def pretty(knight_data: dict):
    """
    Pretty-print the knight data

    :param knight_data: dict of data
    :return:
    """
    pprint(knight_data)
    print()

def get_field(knight_data: dict, knight: str, field_name: str) -> str:
    """
    Retrieve one field from one knight

    :param knight_data:  dict of data
    :param knight: knight name (str)
    :param field_name: field name (str)
    :return:
    """
    return knight_data[knight][field_name]

def print_titles(knight_data: dict):
    """
    Print all knights with their titles to STDOUT
    :param knight_data:  dict of data
    :return:
    """
    for knight, data in knight_data.items():
        print(data["title"], knight)
    print()

if __name__ == '__main__':
    main()





