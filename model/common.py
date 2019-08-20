""" Common functions for models
implement commonly used functions here
"""
import random


def find_id(table, index):
    return table[index][0]


def generate_random(table):
    """
    Generates random and unique string. Used for id/key generation:
         - at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letter
         - it must be unique in the table (first value in every row is the id)

    Args:
        table (list): Data table to work on. First columns containing the keys.

    Returns:
        string: Random and unique string
    """

    generated = ''
    # your code
    table_ids = [row[0] for row in table]
    generated = __generate()
    while generated in table_ids:
        generated = __generate()

    return generated


def __generate():
    special_characters = list(map(chr, range(33, 48)))
    numbers = [str(number) for number in list(range(10))]
    lowercase = list(map(chr, range(97, 123)))
    uppercase = [chr.upper() for chr in lowercase]

    id_special = random.choices(special_characters, k=2)
    id_numbers = random.choices(numbers, k=2)
    id_lowercase = random.choices(lowercase, k=2)
    id_uppercase = random.choices(uppercase, k=2)

    generated = id_special + id_numbers + id_lowercase + id_uppercase
    random.shuffle(generated)
    return ''.join(generated)
