# Modifica el bubble_sort para que funcione de derecha a izquierda, ordenando los números menores primero

def personal_bubble_sort(list):
    
    for other_index in range(len(list)-1):
    
        for index in range(len(list)-1,0,-1):
            current_value = list[index]
            previous_value = list[index-1]
            
            if(current_value < previous_value):
                list[index] = previous_value
                list[index-1] = current_value

    print(list)
my_list = [8,9,7,2,3,1,4,5,6]

personal_bubble_sort(my_list)