""" Inventory module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * name (string): Name of item
    * manufacturer (string)
    * purchase_year (number): Year of purchase
    * durability (number): Years it can be used
"""

# everything you'll need is imported:
from model import data_manager
from model import common


ID = 0
NAME = 1
MANUFACTURER = 2
PURCHASE_YEAR = 3
DURABILITY = 4

CURRENT_YEAR = 2016


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

    return common.add(table, record)


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

    return common.remove(table, id_)


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

    return common.update(table, id_, record)


# special functions:
# ------------------

def get_available_items(table):
    """
    Question: Which items have not exceeded their durability yet?

    Args:
        table (list): data table to work on

    Returns:
        list: list of lists (the inner list contains the whole row with their actual data types)
    """

    # your code
    def is_available(purchase_year, durability):
        return not ((CURRENT_YEAR - int(purchase_year) > int(durability)))

    filtered_table = [item for item in table if is_available(
        item[PURCHASE_YEAR], item[DURABILITY])]

    return [[item[ID], item[NAME], item[MANUFACTURER], int(item[PURCHASE_YEAR]), int(item[DURABILITY])] for item in filtered_table]


def get_average_durability_by_manufacturers(table):
    """
    Question: What are the average durability times for each manufacturer?

    Args:
        table (list): data table to work on

    Returns:
        dict: a dictionary with this structure: { [manufacturer] : [avg] }
    """

    # your code
    def get_durability_average(manufacturer, table):
        durabilities = [item[DURABILITY]
                        for item in table if item[MANUFACTURER] == manufacturer]
        sum_ = 0
        for number in durabilities:
            sum_ += int(number)
        return sum_ / len(durabilities)

    return {item[MANUFACTURER]: get_durability_average(item[MANUFACTURER], table) for item in table}
