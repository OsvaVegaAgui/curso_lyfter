#Ejercicio 7: Cree una función que acepte una lista de números y retorne una lista con los números primos de la misma.

def get_prime_numbers(lista):
    list_numbers_prime =[]
    
    for number in lista:
        if(is_prime(number)):
            list_numbers_prime.append(number)

    return list_numbers_prime

def is_prime(number):
    cont = 1
    prime_number=0
    
    while(cont <= number):
        if(number == 1):
            return False
        else:
            if(number%cont == 0):
                prime_number +=1
            cont +=1
    
    if(prime_number == 2):
        return True
    else:
        return False
    
print(get_prime_numbers([1, 4, 151, 2, 6, 7, 13, 9, 67]))