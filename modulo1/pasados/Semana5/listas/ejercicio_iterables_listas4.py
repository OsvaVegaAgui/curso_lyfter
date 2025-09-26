#Ejercicio4: Cree un programa que elimine todos los números impares de una lista.

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9,11,11,11]
odd_list = []

for index in range(0,len(my_list)):
    if(my_list[index]%2 == 0):
        odd_list.append(my_list[index])
        
my_list = odd_list 
print(my_list)