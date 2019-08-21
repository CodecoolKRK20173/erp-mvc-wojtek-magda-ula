# everything you'll need is imported:
from view import terminal_view
from model.inventory import inventory
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
    DB_FILENAME = 'model/inventory/inventory.csv'
    options = ["Add a new item",
               "Remove a item",
               "Update a item",
               "See available items",
               "See average durability by manufacturers"]
    title_list = ['Id',
                  'Name',
                  'Manufacturer',
                  'Purchase year',
                  'Durability']
    is_running = True
    while is_running is True:
        table = common.get_table(DB_FILENAME)
        choice = terminal_view.get_choice(
            'Inventory menu',
            options,
            'Back to main menu')

        if choice == "1":
            item = terminal_view.get_inputs(
                ['Name: ',
                 'Manufacturer: ',
                 'Purchase year: ',
                 'Durability: '],
                'Please provide item information: ')
            updated_table = inventory.add(table, item)
            common.save_table_to_file(updated_table, DB_FILENAME)
        elif choice == "2":
            terminal_view.print_table(table, title_list)
            index = terminal_view.get_inputs(
                ['Choose Id of an item to be removed: '], '')
            id_ = common.find_id(table, int(index[0]))
            updated_table = inventory.remove(table, id_)
            common.save_table_to_file(updated_table, DB_FILENAME)
        elif choice == "3":
            terminal_view.print_table(table, title_list)
            index = terminal_view.get_inputs(
                ['Choose Id of the item to be edited: '], '')
            id_ = common.find_id(table, int(index[0]))
            item = terminal_view.get_inputs(
                ['Name: ',
                 'Manufacturer: ',
                 'Purchase year: ',
                 'Durability: '],
                'Please provide updated information for this item: ')
            updated_table = inventory.update(table, id_, item)
            common.save_table_to_file(updated_table, DB_FILENAME)
        elif choice == "4":
            filtered_table = inventory.get_available_items(table)
            terminal_view.print_table(filtered_table, title_list)
        elif choice == "5":
            terminal_view.print_result(inventory.get_average_durability_by_manufacturers(
                table), 'Average durability by manufacturer: ')
        elif choice == "0":
            is_running = False
        else:
            terminal_view.print_error_message("There is no such choice.")
