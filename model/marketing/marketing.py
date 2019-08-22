""" Marketing module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * name (string): Name of advertisment
    * objective (string): Objective for this advertisment
    * start_year (number): Year when advertisment was launched
    * end_year (number): Year when advertisment was terminated
    * budget (number): Budget for this advertisment
"""

# everything you'll need is imported:
from model import data_manager
from model import common


ID = 0
NAME = 1
OBJECTIVE = 2
START_YEAR = 3
END_YEAR = 4
BUDGET = 5

CURRENT_YEAR = 2019


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

def get_acive_ads(table):
    """
    Question: Which adverts did not terminate yet?

    Args:
        table (list): data table to work on

    Returns:
        list: list of lists (the inner list contains the whole row with their actual data types)
    """

    # your code
    def is_active(year):
        if not year:
            return True
        else:
            if year == '2019':
                return True
            else:
                return False

    return [ad for ad in table if is_active(ad[END_YEAR])]


def get_average_budget(table):
    """
    Question: What is the average budget for all ads in the table?

    Args:
        table (list): data table to work on

    Returns:
        number: average budget
    """

    # your code
    budgets = [ad[BUDGET] for ad in table]
    sum_ = 0
    for budget in budgets:
        sum_ += float(budget)
    return sum_ / len(budgets)
