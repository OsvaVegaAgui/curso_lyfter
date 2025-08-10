import csv
import os
from datetime import datetime

class Transactions:
    def __init__(self, title, idCategory, amount, date, type, idTransaction=None):
        self.idTransaction = idTransaction
        self.title = title
        self.idCategory = idCategory
        self.amount = amount
        self.date = date
        self.type = type

    def save_transaction(self):
        file_path = os.path.join("modules", "files", "transactions.csv")

        # Título no vacío
        if not self.title.strip():
            return False, "Title cannot be empty"

        # idCategory debe ser número positivo
        try:
            self.idCategory = int(self.idCategory)
            if self.idCategory <= 0:
                return False, "Invalid category ID"
        except ValueError:
            return False, "Category ID must be a number"

        # Monto debe ser número positivo
        try:
            self.amount = float(self.amount)
            if self.amount <= 0:
                return False, "Amount must be greater than zero"
        except ValueError:
            return False, "Amount must be a number"

        # Fecha en formato dd/mm/yyyy
        try:
            datetime.strptime(self.date, "%d/%m/%Y")
        except ValueError:
            return False, "Date must be in format dd/mm/yyyy"

        # El tipo debe ser 1 o 2, doonde 1 es gasto y 2 ingreso
        if str(self.type) not in ["1", "2"]:
            return False, "Type must be 1 (Expense) or 2 (Income)"

        if not os.path.exists(file_path):
            with open(file_path, "w", newline="", encoding="utf-8") as file:
                writer = csv.DictWriter(file, fieldnames=["idTransaction", "title", "idCategory", "amount", "date", "type"])
                writer.writeheader()
                self.idTransaction = 1
                writer.writerow({
                    "idTransaction": self.idTransaction,
                    "title": self.title.strip(),
                    "idCategory": self.idCategory,
                    "amount": self.amount,
                    "date": self.date,
                    "type": self.type
                })
            return True, "Transaction saved successfully"
        else:
            with open(file_path, "r", encoding="utf-8") as file:
                reader = csv.DictReader(file)
                transactions = list(reader)
                if transactions:
                    last_idTransaction = int(transactions[-1]["idTransaction"])
                    self.idTransaction = last_idTransaction + 1
                else:
                    self.idTransaction = 1

            with open(file_path, "a", newline="", encoding="utf-8") as file:
                writer = csv.DictWriter(file, fieldnames=["idTransaction", "title", "idCategory", "amount", "date", "type"])
                writer.writerow({
                    "idTransaction": self.idTransaction,
                    "title": self.title.strip(),
                    "idCategory": self.idCategory,
                    "amount": self.amount,
                    "date": self.date,
                    "type": self.type
                })
            return True, "Transaction saved successfully"

    @staticmethod
    def get_all_transactions():
        file_path = os.path.join("modules", "files", "transactions.csv")
        if not os.path.exists(file_path):
            return []
        with open(file_path, "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            transactions = list(reader)
        return transactions
