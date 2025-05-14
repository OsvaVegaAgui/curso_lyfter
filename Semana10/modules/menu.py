from modules.student_functions import get_student_data, show_registered_students,get_top_three_students,get_general_average
from modules.file_functions import export_student_data,import_student_data


def handle_menu_option(opc,student_list):
    
    
    if(opc == 1):
        student_list = get_student_data()
    elif(opc == 2):
        show_registered_students(student_list)
    elif(opc == 3):
        get_top_three_students(student_list)
    elif(opc == 4):
        get_general_average(student_list)
    elif(opc == 5):
        export_student_data(student_list)
    elif(opc == 6):
        student_list = import_student_data()
        
    return student_list