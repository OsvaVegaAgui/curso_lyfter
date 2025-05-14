from modules.menu import handle_menu_option
class InvalidMenuOption(Exception):
    def __init__(self, opc):
        super().__init__(f"The option {opc} is not valid. Please enter a number between 1 and 7.")

menu_option = 0
student_list = []

while(menu_option != 7):
    try:
        print(' 1. Enter students\n 2. View student information\n 3. View top 3 students\n 4. View general average\n 5. Export all data \n 6. Import data \n 7. Exit \n')
    
        menu_option = int(input("Please select a menu option (1-7): "))
        if menu_option < 1 or menu_option > 7:
            raise InvalidMenuOption(menu_option)
        
        if(menu_option != 7):
            student_list = handle_menu_option(menu_option,student_list)
            
    except InvalidMenuOption as error:
            print(f"Error: {error}")
             
    except ValueError as error:
        print(f'The entered value is not a number. Please enter a valid value {error}')
        
print("The system has been closed.")