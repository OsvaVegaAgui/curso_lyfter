#Cree un programa con un numero secreto del 1 al 10. El programa no debe cerrarse hasta que el usuario adivine el numero.

import random

random_number = random.randint(1, 10)
condition = True

while condition:
    number = int(input("Haz tu intento:"))
    if number == random_number:
        print("¡Has adivinado el número!")
        condition = False
    else:
        print("Intenta de nuevo.")

