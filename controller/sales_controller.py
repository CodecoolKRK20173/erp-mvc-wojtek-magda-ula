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
        table = sales.get_table()
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
            sales.save_table_to_file(updated_table)
        elif choice == "2":
            terminal_view.print_table(table, title_list)
            index = terminal_view.get_inputs(
                ['Choose Id of a sale to be removed: '], '')
            id_ = common.find_id(table, int(index[0]))
            updated_table = sales.remove(table, id_)
            sales.save_table_to_file(updated_table)
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
            sales.save_table_to_file(updated_table)
        elif choice == "4":
            id_ = sales.get_lowest_price_item_id(table)
            terminal_view.print_result(id_, 'ID: ')
        elif choice == "5":
            MONTH_FROM = 0
            DAY_FROM = 1
            YEAR_FROM = 2
            MONTH_TO = 3
            DAY_TO = 4
            YEAR_TO = 5

            dates = terminal_view.get_inputs(
                ['Month from: ',
                 'Day from: ',
                 'Year from: ',
                 'Month to: ',
                 'Day to: ',
                 'Year to: '],
                'Please provide the dates: '
            )
            filtered_table = sales.get_items_sold_between(
                table,
                dates[MONTH_FROM],
                dates[DAY_FROM],
                dates[YEAR_FROM],
                dates[MONTH_TO],
                dates[DAY_TO],
                dates[YEAR_TO]
            )
            terminal_view.print_table(filtered_table, title_list)
        elif choice == "0":
            is_running = False
        else:
            terminal_view.print_error_message("There is no such choice.")
