# everything you'll need is imported:
from view import terminal_view
from model.sales import sales
from controller import common


def run():
    """
    Starts this module and displays its menu.
     * User can access default special features from here.
     * User can go back to main menu from here.

    Returns:
        None
    """

    # your code
    DB_FILENAME = 'model/sales/sales.csv'
    options = ["Add a new sale",
               "Remove a sale",
               "Update a sale",
               "See Id of item which sold for the lowest price",
               "See item sold in a specific date range"]
    title_list = ['Id',
                  'Title',
                  'Price',
                  'Month',
                  'Day',
                  'Year']
    is_running = True
    while is_running is True:
        table = common.get_table(DB_FILENAME)
        terminal_view.print_table(table, title_list)
        choice = terminal_view.get_choice(
            'Sales menu',
            options,
            'Back to main menu')

        if choice == "1":
            sale = terminal_view.get_inputs(
                ['Title',
                 'Price',
                 'Month',
                 'Day',
                 'Year'],
                'Please provide sale information: ')
            updated_table = sales.add(table, sale)
            common.save_table_to_file(updated_table, DB_FILENAME)
        elif choice == "2":
            pass
        elif choice == "3":
            pass
        elif choice == "4":
            pass
        elif choice == "5":
            pass
        elif choice == "0":
            is_running = False
        else:
            terminal_view.print_error_message("There is no such choice.")
