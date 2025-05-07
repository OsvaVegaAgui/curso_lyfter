#Ejercicio2: Cree un programa que intercambie el primer y ultimo elemento de una lista. Debe funcionar con listas de cualquier tamaño

#my_list = [11, 3, 6, 1, 5, 77]

my_list = ["Fin", "y","Inicio"]

first_element = my_list[0]

position_last_element = len(my_list) - 1

last_element = my_list[position_last_element]

for index in range(0,len(my_list)):
    if index == 0:
        my_list[index] = last_element
    elif index == position_last_element:
        my_list[index] = first_element
        
print(my_list)
            
        