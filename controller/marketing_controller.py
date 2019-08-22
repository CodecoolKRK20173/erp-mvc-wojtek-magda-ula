# everything you'll need is imported:
from view import terminal_view
from model.marketing import marketing
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
    DB_FILENAME = 'model/marketing/adverts.csv'
    options = ["Add a new advert",
               "Remove an advert",
               "Update an advert",
               "See active adverts",
               "See average budget for all adverts"]
    title_list = ['Id',
                  'Name',
                  'Role',
                  'Start year',
                  'End year'
                  'Budget']
    is_running = True
    while is_running is True:
        table = common.get_table(DB_FILENAME)
        choice = terminal_view.get_choice(
            'Marketing menu',
            options,
            'Back to main menu')

        if choice == "1":
            pass
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
