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
    DB_FILENAME = 'model/store/games.csv'
    options = ["Add a new game",
               "Remove a game",
               "Update a game",
               "See count of games for each manufacturer",
               "See the average games stock for an specific manufacturer"]
    title_list = ['Id',
                  'Title',
                  'Manufacturer',
                  'Price',
                  'Stock']
    is_running = True
    while is_running is True:
        table = common.get_table(DB_FILENAME)
        terminal_view.print_table(table, title_list)
        choice = terminal_view.get_choice(
            'Store menu',
            options,
            'Back to main menu')

        if choice == "1":
            game = terminal_view.get_inputs(
                ['Title',
                 'Manufacturer',
                 'Price',
                 'in stock'],
                'Please provide game information')
            updated_table = store.add(table, game)
            common.save_table_to_file(updated_table, DB_FILENAME)
        elif choice == "2":
            index = terminal_view.get_inputs(
                ['Choose Id of the game to be removed: '], '')
            id_ = common.find_id(table, int(index[0]))
            updated_table = store.remove(table, id_)
            common.save_table_to_file(updated_table, DB_FILENAME)

        elif choice == "3":
            index = terminal_view.get_inputs(
                ['Choose Id of the game to be edited: '], '')
            id_ = common.find_id(table, int(index[0]))
            game = terminal_view.get_inputs(
                ['Title',
                 'Manufacturer',
                 'Price',
                 'in stock'],
                'Please provide updated information for this game: ')
            updated_table = store.update(table, id_, game)
            common.save_table_to_file(updated_table, DB_FILENAME)
        elif choice == "4":
            terminal_view.print_result(store.get_counts_by_manufacturers(
                table), 'Count of games available for each manufacturer: ')
        elif choice == "5":
            store.get_average_by_manufacturer()
        elif choice == "0":
            is_running = False
        else:
            terminal_view.print_error_message("There is no such choice.")
