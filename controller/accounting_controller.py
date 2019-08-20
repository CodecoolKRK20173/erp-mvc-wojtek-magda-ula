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
    while choice != "0":
        choice = terminal_view.get_choice(options)
        if choice == "1":
            accounting.add()
        elif choice == "2":
            accounting.remove()
        elif choice == "3":
            accounting.update()
        elif choice == "4":
            accounting.which_year_max()
        elif choice == "5":
            accounting.avg_amount()
        else:
            terminal_view.print_error_message("There is no such choice.")
