from modules.interfaces.functions_interfaces import show_add_category_windows, show_add_expense_windows, show_add_income_windows, show_view_data_windows

import FreeSimpleGUI as sg


def show_main_windows():
    layout = [
        [sg.Text("Personal Finance Manager")],
        [sg.Button("Add Category", key="btn_add_category"), sg.Button("Add Expense", key="btn_add_expense"), sg.Button("Add Income", key="btn_add_income"), sg.Button("View transactions", key="btn_view_transactions")],
    ]

    window = sg.Window("Main", layout)

    while True:
        event, values = window.read()
       
        if event == sg.WIN_CLOSED:
            break
        elif event == "btn_add_category":
            show_add_category_windows()
        elif event == "btn_add_expense":
            show_add_expense_windows()
        elif event == "btn_add_income":
            show_add_income_windows()
        elif event == "btn_view_transactions":
            show_view_data_windows()

    window.close()