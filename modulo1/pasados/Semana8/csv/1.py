#Ejercicio 1: Cree un programa que me permita ingresar información de `n` cantidad de videojuegos y los guarde en un archivo `csv`.
    # a. Debe incluir:
    #     1. Nombre
    #     2. Género
    #     3. Desarrollador
    #     4. Clasificación ESRB
import csv

answer="s"
games_list=[]
active = True

def write_csv_file(file_path, data, headers):
    
  with open(file_path, 'w', encoding='utf-8') as file:
    writer = csv.DictWriter(file, headers)
    writer.writeheader()
    writer.writerows(data)

while (active):
    try:
        answer= input("Desea agregar un juego? s/n ")
        
        if answer.lower()!="s" and answer.lower()!="n":
            raise ValueError()
        
        if(answer.lower()=="s"):
            
            name = input("Ingrese el nombre: ")
            genre = input("Ingrese el género: ")
            developer = input("Ingrese el desarrollador: ")
            rating = input("Ingrese la Clasificación ESRB: ")
            
            dictionary_game={
                'name':name,
                'genre':genre,
                'developer':developer,
                'rating':rating
            }
            
            games_list.append(dictionary_game)
        elif(answer.lower()=="n"):  
            active = False
            
    except ValueError as error:
        print(f'El valor ingresado debe ser s o n')
        


write_csv_file('./games.csv', games_list, games_list[0].keys())   

print("Archivo CSV editado con exito") 