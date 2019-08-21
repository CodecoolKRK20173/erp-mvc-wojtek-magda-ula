# everything you'll need is imported:
from view import terminal_view
from model.accounting import accounting
from controller import common


def run():
    """
    Starts this module and displays its menu.
     * User can access default special features from here.
     * User can go back to main menu from here.

    Returns:
        None
    """

    options = ["Add a new record",
               "Remove a record",
               "Update a record",
               "See the highest profit year",
               "See the average profit in a given year"]
    
    table = common.get_table('model/accounting/items.csv')
    title_list = ['Id','Month','Day', 'Year', 'Type', 'Amount (USD)']
    choice = None
    while choice != "0":
        choice = terminal_view.get_choice('Accounting', options, 'Exit program')
        if choice == "1":
            record = terminal_view.get_inputs(['Month: ','Day: ', 'Year: ', 'Type (in or out)', 'Amount in USD: '], "Please provide transaction data you wish to add: ")
            accounting.add(table, record)
        elif choice == "2":
            terminal_view.print_table(table, title_list)
            remove_record_sn = terminal_view.get_inputs([''], "Please provide a number of transaction you wish to remove: ")
            index = remove_record_sn[0]
            id_ = common.find_id(table, index)
            accounting.remove(table, id_)
        elif choice == "3":
            terminal_view.print_table(table, title_list)
            update_record_sn = terminal_view.get_inputs([''], "Please provide a number of transaction you wish to update: ")
            record = terminal_view.get_inputs(['Month: ','Day: ', 'Year: ', 'Type (in or out)', 'Amount in USD: '], "Please provide new data: ")
            index = update_record_sn[0]
            id_ = common.find_id(table, index)
            accounting.update(table, id_, record)
        elif choice == "4":
            accounting.which_year_max(table)
        elif choice == "5":
            user_year = terminal_view.get_inputs(['Year: '], "Please provide a year: ")
            year = int(user_year[0])
            accounting.avg_amount(table, year)
        else:
            terminal_view.print_error_message("There is no such choice.")