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

    choice = None
    table = common.get_table('/model/accounting/items.csv')
    while choice != "0":
        choice = terminal_view.get_choice('Accounting menu', options, 'Back to main menu')

        if choice == "1":
            print("Please provide data you wish to add: ")
            record = []
            record[0] = ''
            record[1] = input('Please provide a month of the transaction: ')
            record[2] = input('Please provide a day of the transaction: ')
            record[3] = input('Please provide a year of the transaction: ')
            record[4] = input(
                'Please provide a type of the transaction (in = income, out = outflow): ')
            is_running = True
            while is_running:
                try:
                    record[5] = int(
                        input('Please provide amount of transaction in USD:'))
                    is_running = False
                except ValueError:
                    print('The value is not an integer!')
            accounting.add(table, record)

        elif choice == "2":
            accounting.remove(table, id_)
        elif choice == "3":
            accounting.update(table, id_, record)
        elif choice == "4":
            accounting.which_year_max(table)
        elif choice == "5":
            accounting.avg_amount(table, year)
        else:
            terminal_view.print_error_message("There is no such choice.")
