# Crea un bubble_sort por tu cuenta sin revisar el código de la lección.

def personal_bubble_sort(list):
    
    for other_index in range(0,len(list)-1):
    
        for index in range(0,len(list)-1-other_index):
            current_value = list[index]
            previous_value = list[index+1]
            
            if(current_value > previous_value):
                list[index] = previous_value
                list[index+1] = current_value

    print(list)
    
my_list = [18, -11, 68, 6, 32, 53, -2]

personal_bubble_sort(my_list)