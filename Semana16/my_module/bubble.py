def bubble_sort(list_to_sort):
    
	if not isinstance(list_to_sort, list):
		raise TypeError("No es una lista")

	for outer_index in range(0, len(list_to_sort) - 1):
		for index in range(0, len(list_to_sort) - 1):
      
			current_element = list_to_sort[index]
			next_element = list_to_sort[index + 1]

			if current_element > next_element:
				list_to_sort[index] = next_element
				list_to_sort[index + 1] = current_element
    
	return list_to_sort

my_test_list = [18, -11, 68, 6, 32, 53, -2]
bubble_sort(my_test_list)