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
    FILE_NAME = 'model/accounting/items.csv'

    options = ["Add a new record",
               "Remove a record",
               "Update a record",
               "See the highest profit year",
               "See the average profit in a given year"]
    
    table = common.get_table('model/accounting/items.csv')
    title_list = ['Id','Month','Day', 'Year', 'Type', 'Amount (USD)']
    is_running = True
    while is_running:
        choice = terminal_view.get_choice('Accounting', options, 'Back to main menu')
        if choice == "1":
            record = terminal_view.get_inputs(['Month: ','Day: ', 'Year: ', 'Type (in or out)', 'Amount in USD: '], "Please provide transaction data you wish to add: ")
            table = accounting.add(table, record)
            common.save_table_to_file(table, FILE_NAME)
        elif choice == "2":
            terminal_view.print_table(table, title_list)
            remove_record_sn = terminal_view.get_inputs([''], "Please provide a number of transaction you wish to remove: ")
            index = int(remove_record_sn[0])
            id_ = common.find_id(table, index)
            table = accounting.remove(table, id_)
            common.save_table_to_file(table, FILE_NAME)
        elif choice == "3":
            terminal_view.print_table(table, title_list)
            update_record_sn = terminal_view.get_inputs([''], "Please provide a number of transaction you wish to update: ")
            record = terminal_view.get_inputs(['Month: ','Day: ', 'Year: ', 'Type (in or out)', 'Amount in USD: '], "Please provide new data: ")
            index = int(update_record_sn[0])
            id_ = common.find_id(table, index)
            table = accounting.update(table, id_, record)
            common.save_table_to_file(table, FILE_NAME)
        elif choice == "4":
            result = accounting.which_year_max(table)
            label = 'A year of the highest profit is'
            terminal_view.print_result(result, label)
        elif choice == "5":
            user_year = terminal_view.get_inputs(['Year: '], "Please provide a year: ")
            year = user_year[0]
            result = accounting.avg_amount(table, year)
            label = 'The average (per item) profit is'
            terminal_view.print_result(result, label)
        elif choice == "0":
            is_running = False
        else:
            terminal_view.print_error_message("There is no such choice.")