#Ejercicio5: Cree un programa que le pida al usuario 10 números, y al final le muestre todos los números que ingresó, seguido del numero ingresado más alto.

numbers_list = []

greater_umber = 0

for index in range(1,11):
    
    number = int(input(f"Digiete le número {index}: "))
    numbers_list.append(number)
    
    if(number > greater_umber):
        greater_umber = number
        
print(f"Los números ingresados fueron: {numbers_list}. El más alto fue: {greater_umber}")
    