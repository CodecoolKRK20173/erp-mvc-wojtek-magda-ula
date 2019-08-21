# everything you'll need is imported:
from view import terminal_view
from model.hr import hr
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
    DB_FILENAME = 'model/hr/persons.csv'
    options = ["Add new record to table",
               "Remove a record with a given id from the table.",
               "Updates specified record in the table",
               "Who is the oldest person?",
               "Who is the closest to the average age?"]
    title_list = ['Id',
    'Person',
    'Year']

    is_running = True
    while is_running is True:
        table = common.get_table(DB_FILENAME)
        terminal_view.print_table(table, title_list)
        choice = terminal_view.get_choice(
            'HR menu',
            options,
            'Back to main menu')


    choice = None
    while choice != "0":
        choice = terminal_view.get_choice(options)
        if choice == "1":
            store_controller.run()
        elif choice == "2":
            hr_controller.run()
        elif choice == "3":
            inventory_controller.run()
        elif choice == "4":
            accounting_controller.run()
        elif choice == "5":
            sales_controller.run()
        elif choice == "6":
            crm_controller.run()
        else:
            terminal_view.print_error_message("There is no such choice.")