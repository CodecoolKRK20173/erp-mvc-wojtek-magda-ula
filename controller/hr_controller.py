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
        #terminal_view.print_table(table, title_list)
        choice = terminal_view.get_choice(
            'HR menu',
            options,
            'Back to main menu')


   
        if choice == "1":
            person = terminal_view.get_inputs(
                ['Person',
                 'Year'],
                'Please provide person information')
            updated_table = hr.add(table, person)
            common.save_table_to_file(updated_table, DB_FILENAME)
        

        elif choice == "2":
            index = terminal_view.get_inputs(
                ['Choose Id of person to be removed: '], '')
            id_ = common.find_id(table, int(index[0]))
            updated_table = hr.remove(table, id_)
            common.save_table_to_file(updated_table, DB_FILENAME)

        
        elif choice == "3":
            index = terminal_view.get_inputs(
                ['Choose Id of person to be edited: '], '')
            id_ = common.find_id(table, int(index[0]))
            person = terminal_view.get_inputs(
                ['Person',
                 'Year'],
                'Please provide updated information of this person: ')
            updated_table = hr.update(table, id_, person)
            common.save_table_to_file(updated_table, DB_FILENAME)
            
        elif choice == "4":
            result = hr.get_oldest_person(table)
            label = "The oldest person are"
            terminal_view.print_result(result, label)
        elif choice == "5":
            result = hr.get_persons_closest_to_average(table)
            label = "The closest average age are"
            terminal_view.print_result(result, label)
        elif choice == "0":
            is_running = False
        else:
            terminal_view.print_error_message("There is no such choice.")