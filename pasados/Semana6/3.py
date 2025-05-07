#Ejercicio 3:Cree una función que retorne la suma de todos los números de una lista.

def sum_list(lista):
    total = 0
    for number in lista:
        total += number
    return total

print(sum_list([1, 1, 1, 3,1]))