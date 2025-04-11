# Cree una calculadora por linea de comando. Esta debe de tener un número actual, y un menú para decidir qué operación hacer con otro número:
# 1. Suma
# 2. Resta
# 3. Multiplicación
# 4. División
# 5. Borrar resultado
# Al seleccionar una opción, el usuario debe ingresar el nuevo número a sumar, restar, multiplicar, o dividir por el actual. El resultado debe pasar a ser el nuevo numero actual.
# Debe de mostrar mensajes de error si el usuario selecciona una opción invalida, o si ingresa un número invalido a la hora de hacer la operación.

class opcionIvalidaMenu(Exception):
    def __init__(self, opc):
        super().__init__(f"La opcion {opc}, no esta dentro del menu, ingresa entre 1 y 6")


number = 0
option = 0
number_entered = 0

def calculate (opc,num):
    
    global number
    
    if(opc == 2):
        number = number + num
    elif(opc == 3):
        number = number - num
    elif(opc == 4):
        number = number * num
    elif(opc == 5):
        
        try:
            number = number / num
        except ZeroDivisionError as e:
            print(f"Error [ZeroDivisionError]: Intentaste dividir {number} entre 0. Detalles: {e}")
        
    elif(opc == 1):
        number = 0

while (option != 6):
    try:
        print(f"Valor Actual: {number}")
        print("#### MENU CALCULADORA #### ")
        print("1. Limpiar")
        print("2. Sumar")
        print("3. Restar")
        print("4. Multiplicar")
        print("5. Dividir")
        print("6. Salir")
        
        try:
            option = int(input("Seleccione una opcion: "))
            if option < 1 or option > 6:
                raise opcionIvalidaMenu(option)
            
            number_entered = int(input("Digite un numero: "))
            calculate (option,number_entered )
            
        except opcionIvalidaMenu as error:
             print(f"Error detectado: {error}")
        
    except ValueError as error:
        print(f'El valor ingresado no es un numero, por favor digite un valor valido {error}')
        
print("Calculadora cerrada")