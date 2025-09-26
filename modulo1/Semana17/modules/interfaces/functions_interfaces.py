import FreeSimpleGUI as sg

from modules.logica.Categorias import Categorias
from modules.logica.Transactions import Transactions

# VENTANA PARA INGRESAR CATEGORIAS
def show_add_category_windows():
    
    layout = [
        [sg.Text("Name category:"), sg.Input(key="txt_category_name")],
        [sg.Push(),sg.Button("Add",key="btn_save_category" ,pad=(0,20) ,size=(18, 1)), sg.Push()]
    ]

    window = sg.Window("Add Category", layout)

    while True:
        event, values = window.read()
    
        if event == sg.WIN_CLOSED:
            break
        elif event == "btn_save_category":
            
            # CONECTAR LA CLASE, CREAR LA CATEGORIA Y GUARDARLA EN EL ARCHIVO
            
            category_name = values["txt_category_name"]
            
            categoria = Categorias(category_name)
            
            success, message = categoria.save_category()
            sg.popup(message)
            
            if success:
                window["txt_category_name"].update("")
            
    window.close()
   
#VENTANA PARRA AGREGAR GASTOS 
def show_add_expense_windows():
    
    categories = Categorias.get_all_categories()
    categories_names = []
    for category in categories:
        categories_names.append(category["name"])
    
    layout = [
        [sg.Text("Expense name:", size=(13, 1)), sg.Input(key="txt_expense_name")],
        [sg.Text("Amount:", size=(13, 1)), sg.Input(key="txt_amount")],
        [sg.Text("Category:", size=(13, 1)), sg.Combo(values=categories_names, key="cmb_category")],
        [sg.Text("Date (dd/mm/yyyy):", size=(13, 1)), sg.Input(key="txt_date")],
        [sg.Push(), sg.Button("Save", key="btn_save_expense", pad=(0, 20), size=(18, 1)), sg.Push()]
    ]

    window = sg.Window("Add Expense", layout)

    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED:
            break
        elif event == "btn_save_expense":
            
            selected_category_name = values["cmb_category"]
            idCategory = None
            for category in categories:
                if category["name"] == selected_category_name:
                    idCategory = category["idCategoria"]
                    break
                
            transaction = Transactions(
                title=values["txt_expense_name"],
                idCategory=idCategory,
                amount=values["txt_amount"],
                date=values["txt_date"],
                type=1
            )
            
            success, message = transaction.save_transaction()
            sg.popup(message)
            
            if success:
                window["txt_expense_name"].update("")
                window["txt_amount"].update("")
                window["cmb_category"].update("")
                window["txt_date"].update("")

    window.close()

#VENTANA PARA AGREGAR INGRESOS 
def show_add_income_windows():
    
    categories = Categorias.get_all_categories()
    categories_names = []
    for category in categories:
        categories_names.append(category["name"])
    
    layout = [
        [sg.Text("Income name:", size=(13, 1)), sg.Input(key="txt_income_name")],
        [sg.Text("Amount:", size=(13, 1)), sg.Input(key="txt_income_amount")],
        [sg.Text("Category:", size=(13, 1)), sg.Combo(values=categories_names, key="cmb_income_category")],
        [sg.Text("Date (dd/mm/yyyy):", size=(13, 1)), sg.Input(key="txt_income_date")],
        [sg.Push(), sg.Button("Save", key="btn_save_income", pad=(0, 20), size=(18, 1)), sg.Push()]
    ]

    window = sg.Window("Add Income", layout)

    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED:
            break
        elif event == "btn_save_income":
          
            selected_category_name = values["cmb_income_category"]
            idCategory = None
            for category in categories:
                if category["name"] == selected_category_name:
                    idCategory = category["idCategoria"]
                    break
            
            transaction = Transactions(
                title=values["txt_income_name"],
                idCategory=idCategory,
                amount=values["txt_income_amount"],
                date=values["txt_income_date"],
                type=2
            )
            
            success, message = transaction.save_transaction()
            sg.popup(message)

            if success:
                window["txt_income_name"].update("")
                window["txt_income_amount"].update("")
                window["cmb_income_category"].update("")
                window["txt_income_date"].update("")
    window.close()
    
# VENTANA PARA VISUALIZAR TODOS LOS transactionIMIENTOS
def show_view_data_windows():
    
    transactions = Transactions.get_all_transactions()
    all_categories = Categorias.get_all_categories()

    categories = {}
    for category in all_categories:
        categories[category["idCategoria"]] = category["name"]

    table_data = []
    total_expenses = 0
    total_incomes = 0

    for transaction in transactions:
        
        category_name = ""
        for key, value in categories.items():
            if key == transaction["idCategory"]:
                category_name = value
                break
        
        expense_col = ""
        income_col = ""

        if transaction["type"] == "1":
            
            expense_col = transaction["amount"]
            total_expenses += float(transaction["amount"])
            
        elif transaction["type"] == "2":
            
            income_col = transaction["amount"]
            total_incomes += float(transaction["amount"])

        table_data.append([
            transaction["title"],
            category_name,
            expense_col,
            income_col
        ])

    balance = total_incomes - total_expenses

    layout = [
        [sg.Text("Transactions", font=("Arial", 14, "bold"))],
        [sg.Table(
            values=table_data,
            headings=["Title", "Category", "Expense", "Income"],
            auto_size_columns=False,
            col_widths=[20, 15, 10, 10],
            justification="center",
            key="tbl_transactions",
            num_rows=min(15, len(table_data))
        )],
        [sg.Text(f"Total Incomes: ₡{total_incomes:,.2f}", text_color="green"),
        sg.Text(f"Total Expenses: ₡{total_expenses:,.2f}", text_color="yellow"),
         sg.Text(f"Net Balance: ₡{balance:,.2f}", text_color="white")],
        [sg.Button("Close")]
    ]

    window = sg.Window("View Transactions", layout, finalize=True)

    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, "Close"):
            break

    window.close()

   