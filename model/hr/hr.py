""" Human resources module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * name (string)
    * birth_year (number)
"""

# everything you'll need is imported:
from model import data_manager
from model import common

ID = 0
PERSON_NAME = 1
YEAR = 2



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
    
    id = common.generate_random(table)
    record.insert(0, id)
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
    def find_record_index(id_):
        for index, record in enumerate(table):
            if record[ID] == id_:
                return index

    record_index = find_record_index(id_)
    table[record_index][PERSON_NAME], table[record_index][YEAR] = record
    return table


# special functions:
# ------------------

def get_oldest_person(table):
    """
    Question: Who is the oldest person?

    Args:
        table (list): data table to work on

    Returns:
        list: A list of strings (name or names if there are two more with the same value)
    """

    # your code
    min_year = int(table[0][YEAR])

    for person in table:        
        if int(person[YEAR]) < min_year:
            min_year = int(person[YEAR])

    selected_people = []
    for person in table:
        if int(person[YEAR]) == min_year:
            selected_people.append(person[PERSON_NAME])

    return selected_people



def get_persons_closest_to_average(table):
    """
    Question: Who is the closest to the average age?

    Args:
        table (list): data table to work on

    Returns:
        list: list of strings (name or names if there are two more with the same value)
    """

    # your code
    # record = int(table[YEAR])
    # divide_number = 10

    # for person in table:
    #     if int(person[YEAR]) == record:

    calc = 0
    for person in table:
        calc = calc + int(person[YEAR])
    avg = calc / len(table)
    
    # diff = 0
    # diff = int(person[YEAR]) - avg
    # for person in table: 
    #     diff = int(person[YEAR]) - avg
    #     if avg > diff:
    #         person = 

    first_list_in_table = 0
    min_diff = abs(avg - (int(table[first_list_in_table][YEAR])))
    year_of_min_diff = table[first_list_in_table][YEAR]
    for person in table:
        diff = abs(avg - int(person[YEAR]))
        if diff < min_diff:
            min_diff = diff
            year_of_min_diff = person[YEAR]
    
    selected_people = []
    for person in table:
        if int(person[YEAR]) == int(year_of_min_diff):
            selected_people.append(person[PERSON_NAME])

    return selected_people




