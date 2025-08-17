#Ejercicio2 Diccionarios: Cree un programa que cree un diccionario usando dos listas del mismo tamaño, usando una para sus keys, y la otra para sus values.

list_a = ['first_name', 'last_name', 'role']
list_b = ['Osvaldo', 'Vega', 'Software Engineer']

dictionary = {
     list_a[0]:list_b[0],
     list_a[1]:list_b[1],
     list_a[2]:list_b[2]
}

#dictionary = {list_a[index]: list_b[index] for index in range(0, len(list_a))}

print(dictionary)