""" Common functions for models
implement commonly used functions here
"""
import random


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
    special_characters = list(map(chr, range(33, 39))) + \
        list(map(chr, range(40, 48)))
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


def add(table, record):
    """
    Add new record to table

    Args:
        table (list): table to add new record to
        record (list): new record

    Returns:
        list: Table with a new record
    """
    # your code
    id_ = generate_random(table)
    record.insert(0, id_)
    table.append(record)
    return table


def remove(table, id_):
    """
    Remove a record with a given id from the table.

    Args:
        table (list): table to remove a record from
        id_ (str): id of a record to be removed

    Returns:
        list: Table without specified record.
    """

    # your code
    ID = 0
    table = [record for record in table if record[ID] != id_]
    return table


def update(table, id_, record):
    """
    Updates specified record in the table.

    Args:
        table: list in which record should be updated
        id_ (str): id of a record to update
        record (list): updated record

    Returns:
        list: table with updated record
    """

    # your code
    ID = 0

    def find_record_index(id_):
        for index, record in enumerate(table):
            if record[ID] == id_:
                return index

    record_index = find_record_index(id_)

    record.insert(0, 'fake_id')
    for i, _ in enumerate(record):
        if i == ID:
            pass
        else:
            table[record_index][i] = record[i]

    return table
