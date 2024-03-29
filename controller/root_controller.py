# everything you'll need is imported:
from view import terminal_view
from controller import store_controller
from controller import hr_controller
from controller import inventory_controller
from controller import accounting_controller
from controller import sales_controller
from controller import crm_controller
from controller import marketing_controller
from controller import common


def run():
    options = ["Store manager",
               "Human resources manager",
               "Inventory manager",
               "Accounting manager",
               "Sales manager",
               "Customer Relationship Management (CRM)",
               "Marketing manager"]

    is_running = True
    while is_running is True:
        choice = terminal_view.get_choice('Main menu', options, 'Exit program')
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
        elif choice == "7":
            marketing_controller.run()
        elif choice == "0":
            is_running = False
        else:
            terminal_view.print_error_message("There is no such choice.")
