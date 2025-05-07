#Cree un programa que le pida tres números al usuario y muestre el mayor.

number1 = int(input("Ingrese el primer número: "))
number2 = int(input("Ingrese el segundo número: "))
number3 = int(input("Ingrese el tercer número: "))

if(number1 > number2 and number1 > number3):
    print(f"El número mayor es el primero {number1}.")
elif(number2 > number3):
    print(f"El número mayor es el segundo {number2}.")
else:
    print(f"El número mayor es el tercero {number3}.")