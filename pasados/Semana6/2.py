#Ejercicio 2: Experimente con el concepto de scope:
    # 1. Intente accesar a una variable definida dentro de una función desde afuera.
    # 2.  Intente accesar a una variable global desde una función y cambiar su valor.
    

global_var = "Osvaldo"

def print_var():
    print(f"Este es mi nombre: {global_var}")
    internal_var = "Vega"

print_var()

print(f"Esta es mi apellido: {internal_var}")