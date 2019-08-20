# everything you'll need is imported:
from model.store import store
from view import terminal_view
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
    table = common.get_table('model/store/games.csv')
    options = ["Add a new game",
               "Remove a game",
               "Update a game",
               "See count of game kinds for each manufacturer",
               "See the average games stock for an specific manufacturer"]
    title_list = ['Id',
                  'Title',
                  'Manufacturer',
                  'Price',
                  'Stock']
    is_running = True
    while is_running is True:
        terminal_view.print_table(table, title_list)
        choice = terminal_view.get_choice(
            'Store menu',
            options,
            'Back to main menu')

        if choice == "1":
            game = terminal_view.get_inputs(
                ['Title', 'Manufacturer', 'Price', 'in stock'],
                'Please provide game information')
            common.save_table_to_file(
                store.add(table, game),
                'model/store/games.csv')
        elif choice == "2":
            store.remove()
        elif choice == "3":
            store.update()
        elif choice == "4":
            store.get_counts_by_manufacturers()
        elif choice == "5":
            store.get_average_by_manufacturer()
        elif choice == "0":
            is_running = False
        else:
            terminal_view.print_error_message("There is no such choice.")
