#Ejercicio 1: Cree un programa que lea nombres de canciones de un archivo (línea por línea) y guarde en otro archivo los mismos nombres ordenados alfabéticamente.
songs_list = []
songs_order = []

def write_text_to_file(file_path, list):
    with open(file_path, 'a', encoding='utf-8') as file:
        for index in range(0, len(list)):
            file.write(list[index] + '\n')  

def open_and_print_file_per_line(path):
    with open(path, 'r', encoding='utf-8') as file:
        for line in file.readlines():
            songs_list.append(line)

    songs_order = sorted(songs_list)
    write_text_to_file('ordenadas.txt', songs_order)

open_and_print_file_per_line('canciones.txt')
