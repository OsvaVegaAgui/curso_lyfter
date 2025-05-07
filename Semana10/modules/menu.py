from modules.student_functions import get_student_data, show_registered_students,get_top_three_students,get_general_average
from modules.file_functions import export_student_data,import_student_data


def handle_menu_option(opc):
    if(opc == 1):
        get_student_data()
    elif(opc == 2):
        show_registered_students()
    elif(opc == 3):
        get_top_three_students()
    elif(opc == 4):
        get_general_average()
    elif(opc == 5):
        export_student_data()
    elif(opc == 6):
        import_student_data()