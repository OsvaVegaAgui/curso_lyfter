from modules.config import student_list
from modules.config import InvalidGrade

def get_valid_grade(subject):
    while True:
        try:
            grade = float(input(f"Enter the grade for {subject}: "))
            if grade < 0 or grade > 100:
                raise InvalidGrade(grade)
            return grade
        except InvalidGrade as error:
            print(f"Error: {error}")
        except ValueError as error:
            print(f'The entered value is not a number. Please enter a valid value. ({error})')

def get_student_data():
    
    another_student = ""
    
    while(another_student != "no"):
        
        full_name = input("\n Enter the student's full name: ")
        section = input("Enter the student's section: ")
        
        spanish_grade = get_valid_grade("Spanish")
        english_grade = get_valid_grade("English")
        social_studies_grade = get_valid_grade("Social Studies")
        science_grade = get_valid_grade("Science")

        student_average_grade = (spanish_grade+english_grade+social_studies_grade+science_grade)/4
        
        student ={
            "average":student_average_grade,
            "name":full_name,
            "section":section,
            "spanish":spanish_grade,
            "english":english_grade,
            "social_studies":social_studies_grade,
            "science":science_grade,
        }
        
        student_list.append(student)
        
        another_student = input("Do you want to add another student? (yes/no): ").lower()

def show_registered_students():
    
    for index in range(0, len(student_list)):
        
        print(f"Student name: {student_list[index]['name']} \n")
        print(f"Section: {student_list[index]['section']} \n")
        print(f"Average: {student_list[index]['average']} \n")
        print("Grades by subject: \n")
        
        print(f"\t Spanish: {student_list[index]['spanish']} \n")
        print(f"\t English: {student_list[index]['english']} \n")
        print(f"\t Social Studies: {student_list[index]['social_studies']} \n")
        print(f"\t Science: {student_list[index]['science']} \n")
        
        print(" --------------- * --------------- \n")

def get_top_three_students():
              
    sorted_students = sorted(student_list, key=lambda student: student["average"], reverse=True)
    
    print("+++++++ TOP 3 STUDENTS BY AVERAGE GRADE +++++++ \n")

    for index in range(min(3, len(sorted_students))):
        print(f"#{index+1} {sorted_students[index]['name']}: {sorted_students[index]['average']}\n")

def get_general_average():
    
    try:
        
        total_average_sum = 0

        student_count = len(student_list)

        for student in student_list:
            total_average_sum += student['average']
            
        general_average = round((total_average_sum/student_count),2)
        
        print(f"\n The general average is: {general_average } \n")
        
    except ZeroDivisionError as e:
            print(f"\n You tried to divide by zero. Details: {e} \n")