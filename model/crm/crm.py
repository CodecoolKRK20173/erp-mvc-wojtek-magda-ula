""" Customer Relationship Management (CRM) module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * name (string)
    * email (string)
    * subscribed (int): Is she/he subscribed to the newsletter? 1/0 = yes/no
"""

# everything you'll need is imported:
from model import data_manager
from model import common

ID_INDEX = 0
NAME_INDEX = 1
E_MAIL_INDEX = 2 
SUBSCRIPTION_INDEX = 3


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

def get_longest_name_id(table):
    """
        Question: What is the id of the customer with the longest name?

        Args:
            table (list): data table to work on

        Returns:
            string: id of the longest name (if there are more than one, return
                the last by alphabetical order of the names)
        """
    max_len_names = []
    max_lenght = 0
    for single_list in table:
        if len(single_list[NAME_INDEX]) >= max_lenght:
            max_lenght = len(single_list[NAME_INDEX]) 
            max_len_names.append(single_list[NAME_INDEX])
    if len(max_len_names) == 1:
        max_len_name = max_len_names[0]
    else:
        max_len_name = ''
        for element in max_len_names:
            if element > max_len_name:
                max_len_name = element

    for single_list in table:
        if single_list[NAME_INDEX] == max_len_name:
            return single_list[ID_INDEX]


# the question: Which customers has subscribed to the newsletter?
# return type: list of strings (where string is like email+separator+name, separator=";")
def get_subscribed_emails(table):
    """
        Question: Which customers has subscribed to the newsletter?

        Args:
            table (list): data table to work on

        Returns:
            list: list of strings (where a string is like "email;name")
        """

    subscribers = {}
    subscribers_list = []

    for single_list in table:
        if int(single_list[SUBSCRIPTION_INDEX]) == 1:
            subscribers[single_list[E_MAIL_INDEX]] = single_list[NAME_INDEX]

    for key, value in subscribers.items():
        subscriber = key + ';' + value
        subscribers_list.append(subscriber)
    return subscribers_list
