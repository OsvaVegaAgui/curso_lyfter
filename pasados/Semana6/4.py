#Ejercicio 4:Cree una función que le de la vuelta a un string y lo retorne

def get_text(my_string):
    inicio = len(my_string)-1
    texto = ""
    
    for index in range(inicio,-1,-1):
        texto += my_string[index]
        
    return texto

print(get_text("Pizza con piña"))