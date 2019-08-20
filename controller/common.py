""" Common functions for controllers
implement commonly used functions here
"""
from model import data_manager


def get_table(file_name):
    return data_manager.get_table_from_file(file_name)


def save_table_to_file(table, file_name):
    data_manager.write_table_to_file(file_name, table)


def find_id(table, index):
    return table[index][0]
    