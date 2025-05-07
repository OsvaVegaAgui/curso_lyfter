#Ejercicio 1: Cree dos funciones que impriman dos cosas distintas, y haga que la primera llame la segunda.

def print_one():
    print("Esta es la primera funcion")
    print_two()
    
def print_two():
    print("Esta es la segunda funcion")
    
print_one()