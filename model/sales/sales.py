""" Sales module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * title (string): Title of the game sold
    * price (number): The actual sale price in USD
    * month (number): Month of the sale
    * day (number): Day of the sale
    * year (number): Year of the sale
"""

# everything you'll need is imported:
from model import data_manager
from model import common


ID = 0
TITLE = 1
PRICE = 2
MONTH = 3
DAY = 4
YEAR = 5


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

def get_lowest_price_item_id(table):
    """
    Question: What is the id of the item that was sold for the lowest price?
    if there are more than one item at the lowest price, return the last item by alphabetical order of the title

    Args:
        table (list): data table to work on

    Returns:
         string: id
    """

    # your code
    def bubble_sort(lst):
        for index in range(len(lst)):
            for j in range(0, len(lst) - index - 1):
                if lst[j] > lst[j+1]:
                    lst[j], lst[j+1] = lst[j+1], lst[j]
        return lst

    min_price = 999
    for sale in table:
        try:
            sale_price = int(sale[PRICE])
        except ValueError:
            sale_price = float(sale[PRICE])

        if sale_price < min_price:
            min_price = sale_price

    lowest_priced_items = [sale[TITLE]
                           for sale in table if sale[PRICE] == str(min_price)]

    if len(lowest_priced_items) > 1:
        lowest_priced_items_sorted = bubble_sort(lowest_priced_items)
        result = lowest_priced_items_sorted[-1]
    else:
        result = lowest_priced_items[0]

    return [sale[ID] for sale in table if sale[TITLE] == result][0]


def get_items_sold_between(table, *dates):
    """
    Question: Which items are sold between two given dates? (from_date < sale_date < to_date)

    Args:
        table (list): data table to work on
        month_from (int)
        day_from (int)
        year_from (int)
        month_to (int)
        day_to (int)
        year_to (int)

    Returns:
        list: list of lists (the filtered table)
    """

    # your code
    MONTH_FROM = 0
    DAY_FROM = 1
    YEAR_FROM = 2
    MONTH_TO = 3
    DAY_TO = 4
    YEAR_TO = 5
    dates = [int(date) for date in dates]
    return [sale for sale in table
            if dates[MONTH_FROM] <= int(sale[MONTH]) <= dates[MONTH_TO]
            if dates[DAY_FROM] <= int(sale[DAY]) <= dates[DAY_TO]
            if dates[YEAR_FROM] <= int(sale[YEAR]) <= dates[YEAR_TO]
            ]
