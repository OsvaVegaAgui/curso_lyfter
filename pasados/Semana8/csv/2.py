#Ejercicio 2: cree una version alternativa del ejercicio 1 que guarde el archivo separado por tabulaciones en vez de por comas.
import csv

answer="s"
games_list=[]
active = True

def write_csv_file(file_path, data, headers):
    
  with open(file_path, 'w', encoding='utf-8', newline='') as file:
    writer = csv.DictWriter(file, headers, delimiter='\t')
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
        


write_csv_file('./games2.csv', games_list, games_list[0].keys())   

print("Archivo CSV editado con exito") 