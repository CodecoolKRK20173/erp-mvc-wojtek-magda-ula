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

    return table


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

    year_index = 3
    type_index = 4
    amount_index = 5
    year_profit = {}
    max_profit = 0
    for single_list in table:
        if single_list[year_index] in year_profit.keys():
            if single_list[type_index] == "in":
                year_profit[single_list[year_index]] += float(single_list[amount_index])
            elif single_list[type_index] == "out":
                year_profit[single_list[year_index]] -= float(single_list[amount_index])
        else:
            if single_list[type_index] == "in":
                year_profit[single_list[year_index]] = float(single_list[amount_index])
            elif single_list[type_index] == "out":
                year_profit[single_list[year_index]] = -(float(single_list[amount_index]))
    for key, value in year_profit.items():
        if value > max_profit:
            max_profit = value
            max_profit_year = key
    
    return max_profit_year

           




def avg_amount(table, year):
    """
    Question: What is the average (per item) profit in a given year? [(profit)/(items count)]

    Args:
        table (list): data table to work on
        year (number)

    Returns:
        number
    """

    # your code
