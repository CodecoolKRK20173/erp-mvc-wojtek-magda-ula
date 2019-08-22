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
                  'Objective',
                  'Start year',
                  'End year',
                  'Budget']
    is_running = True
    while is_running is True:
        table = common.get_table(DB_FILENAME)
        choice = terminal_view.get_choice(
            'Marketing menu',
            options,
            'Back to main menu')

        if choice == "1":
            game = terminal_view.get_inputs(
                ['Name',
                 'Objective',
                 'Start year',
                 'End year',
                 'Budget'],
                'Please provide advert information')
            updated_table = marketing.add(table, game)
            common.save_table_to_file(updated_table, DB_FILENAME)
        elif choice == "2":
            terminal_view.print_table(table, title_list)
            index = terminal_view.get_inputs(
                ['Choose Id of the advert to be removed: '], '')
            id_ = common.find_id(table, int(index[0]))
            updated_table = marketing.remove(table, id_)
            common.save_table_to_file(updated_table, DB_FILENAME)
        elif choice == "3":
            terminal_view.print_table(table, title_list)
            index = terminal_view.get_inputs(
                ['Choose Id of the advert to be edited: '], '')
            id_ = common.find_id(table, int(index[0]))
            game = terminal_view.get_inputs(
                ['Name',
                 'Objective',
                 'Start year',
                 'End year',
                 'Budget'],
                'Please provide updated information for this game: ')
            updated_table = marketing.update(table, id_, game)
            common.save_table_to_file(updated_table, DB_FILENAME)
        elif choice == "4":
            ads = marketing.get_acive_ads(table)
            terminal_view.print_table(ads, title_list)
        elif choice == "5":
            avg_budget = marketing.get_average_budget(table)
            terminal_view.print_result(
                avg_budget, 'Average budget for all adverts: ')
        elif choice == "0":
            is_running = False
        else:
            terminal_view.print_error_message("There is no such choice.")
