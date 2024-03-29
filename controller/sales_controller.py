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
            terminal_view.print_table(table, title_list)
            index = terminal_view.get_inputs(
                ['Choose Id of a sale to be removed: '], '')
            id_ = common.find_id(table, int(index[0]))
            updated_table = sales.remove(table, id_)
            common.save_table_to_file(updated_table, DB_FILENAME)
        elif choice == "3":
            terminal_view.print_table(table, title_list)
            index = terminal_view.get_inputs(
                ['Choose Id of the sale to be edited: '], '')
            id_ = common.find_id(table, int(index[0]))
            sale = terminal_view.get_inputs(
                ['Title',
                 'Price',
                 'Month',
                 'Day',
                 'Year'],
                'Please provide updated information for this sale: ')
            updated_table = sales.update(table, id_, sale)
            common.save_table_to_file(updated_table, DB_FILENAME)
        elif choice == "4":
            id_ = sales.get_lowest_price_item_id(table)
            terminal_view.print_result(id_, 'ID')
        elif choice == "5":
            dates = terminal_view.get_inputs(
                ['Month from: ',
                 'Day from: ',
                 'Year from: ',
                 'Month to: ',
                 'Day to: ',
                 'Year to: '],
                'Please provide the dates: '
            )
            month_from, day_from, year_from, month_to, day_to, year_to = dates
            filtered_table = sales.get_items_sold_between(
                table,
                month_from,
                day_from,
                year_from,
                month_to,
                day_to,
                year_to
            )
            print(filtered_table)
            terminal_view.print_table(filtered_table, title_list)
        elif choice == "0":
            is_running = False
        else:
            terminal_view.print_error_message("There is no such choice.")
