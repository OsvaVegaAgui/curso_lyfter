import csv
import os

class Categorias:
    
    def __init__(self, name, idCategoria=None):
        self.idCategoria = idCategoria
        self.name = name

    def save_category(self):
        file_path = os.path.join("modules", "files", "categorias.csv")
        
        self.name = self.name.strip()
        
        if not self.name:
            return False, "Please enter a category name"

        # Si el archivo no existe lo crea
        if not os.path.exists(file_path):
            with open(file_path, "w", newline="", encoding="utf-8") as file:
                writer = csv.DictWriter(file, fieldnames=["idCategoria", "name"])
                writer.writeheader()
                self.idCategoria = 1
                writer.writerow({"idCategoria": self.idCategoria, "name": self.name})
                
                return True, "Category saved successfully"
        else:
            
            #Obtener el ultimo id
            with open(file_path, "r", encoding="utf-8") as file:
                reader = csv.DictReader(file)
                categorias = list(reader)
                
                #Se verifica si la categoria ya existe
                for categoria in categorias:
                    if categoria["name"].strip().lower() == self.name.lower():
                        return False, "This category already exists"
                
                if categorias:
                    last_idCategoria = int(categorias[-1]["idCategoria"])
                    self.idCategoria = last_idCategoria + 1
                else:
                    self.idCategoria = 1

            #Agregar al archivo la nueva categoria
            with open(file_path, "a", newline="", encoding="utf-8") as file:
                writer = csv.DictWriter(file, fieldnames=["idCategoria", "name"])
                writer.writerow({"idCategoria": self.idCategoria, "name": self.name})
                
                return True, "Category saved successfully"

    @staticmethod
    def get_all_categories():
        file_path = os.path.join("modules", "files", "categorias.csv")

        if not os.path.exists(file_path):
            return []

        with open(file_path, "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            categorias = list(reader)

        return categorias