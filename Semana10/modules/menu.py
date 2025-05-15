from modules.student_functions import get_student_data, show_registered_students,get_top_three_students,get_general_average
from modules.file_functions import export_student_data,import_student_data


def menu():
    class InvalidMenuOption(Exception):
        def __init__(self, opc):
            super().__init__(f"The option {opc} is not valid. Please enter a number between 1 and 7.")
            
    student_list = []
    
    while(True):
        try:
            print(' 1. Enter students\n 2. View student information\n 3. View top 3 students\n 4. View general average\n 5. Export all data \n 6. Import data \n 7. Exit \n')
        
            menu_option = int(input("Please select a menu option (1-7): "))
            if menu_option < 1 or menu_option > 7:
                raise InvalidMenuOption(menu_option)
            
            if(menu_option == 1):
                student_list = get_student_data()
            elif(menu_option == 2):
                show_registered_students(student_list)
            elif(menu_option == 3):
                get_top_three_students(student_list)
            elif(menu_option == 4):
                get_general_average(student_list)
            elif(menu_option == 5):
                export_student_data(student_list)
            elif(menu_option == 6):
                student_list = import_student_data()
            else:
                break
                
        except InvalidMenuOption as error:
                print(f"Error: {error}")
                
        except ValueError as error:
            print(f'The entered value is not a number. Please enter a valid value {error}')
            
    print("The system has been closed.")