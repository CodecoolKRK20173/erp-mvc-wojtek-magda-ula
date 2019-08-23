""" Accounting module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * month (number): Month of the transaction
    * day (number): Day of the transaction
    * year (number): Year of the transaction
    * type (string): in = income, out = outflow
    * amount (int): amount of transaction in USD
"""

# everything you'll need is imported:
from model import data_manager
from model import common


ID_INDEX = 0
MONTH_INDEX = 1
DAY_INDEX = 2
YEAR_INDEX = 3
TYPE_INDEX = 4
AMOUNT_INDEX = 5


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

def which_year_max(table):
    """
    Question: Which year has the highest profit? (profit = in - out)

    Args:
        table (list): data table to work on

    Returns:
        number
    """

    year_profit = {}
    max_profit = 0
    for single_list in table:
        if single_list[YEAR_INDEX] in year_profit.keys():
            if single_list[TYPE_INDEX] == "in":
                year_profit[single_list[YEAR_INDEX]] += float(single_list[AMOUNT_INDEX])
            elif single_list[TYPE_INDEX] == "out":
                year_profit[single_list[YEAR_INDEX]] -= float(single_list[AMOUNT_INDEX])
        else:
            if single_list[TYPE_INDEX] == "in":
                year_profit[single_list[YEAR_INDEX]] = float(single_list[AMOUNT_INDEX])
            elif single_list[TYPE_INDEX] == "out":
                year_profit[single_list[YEAR_INDEX]] = -(float(single_list[AMOUNT_INDEX]))
    for key, value in year_profit.items():
        if value > max_profit:
            max_profit = value
            max_profit_year = key
    
    return int(max_profit_year)

           




def avg_amount(table, year):
    """
    Question: What is the average (per item) profit in a given year? [(profit)/(items count)]

    Args:
        table (list): data table to work on
        year (number)

    Returns:
        number
    """
    year_profit = {}
    year_items_count = {}
    for single_list in table:
        if single_list[YEAR_INDEX] in year_profit.keys():
            if single_list[TYPE_INDEX] == "in":
                year_profit[single_list[YEAR_INDEX]] += float(single_list[AMOUNT_INDEX])
            elif single_list[TYPE_INDEX] == "out":
                year_profit[single_list[YEAR_INDEX]] -= float(single_list[AMOUNT_INDEX])
            year_items_count[single_list[YEAR_INDEX]] += 1
        else:
            if single_list[TYPE_INDEX] == "in":
                year_profit[single_list[YEAR_INDEX]] = float(single_list[AMOUNT_INDEX])
            elif single_list[TYPE_INDEX] == "out":
                year_profit[single_list[YEAR_INDEX]] = -(float(single_list[AMOUNT_INDEX]))
            year_items_count[single_list[YEAR_INDEX]] = 1
    
    profit = float(year_profit[year])
    items_count = float(year_items_count[year])

    return str(round((profit/items_count),2))
    

