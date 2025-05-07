#Ejercicio2: Cree un programa que itere e imprima un string letra por letra de derecha a izquierda

my_string = 'Pizza con piña'
inicio = len(my_string)-1

for index in range(inicio,-1,-1):
    print(my_string[index])