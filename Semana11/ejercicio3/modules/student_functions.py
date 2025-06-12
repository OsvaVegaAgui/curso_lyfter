class Student():
    def __init__(self, average,name,section,spanish,english,social_studies,science):
        self.average = average
        self.name = name
        self.section = section
        self.spanish = spanish
        self.english = english
        self.social_studies = social_studies
        self.science = science

class InvalidGrade(Exception):
    def __init__(self, grade):
        super().__init__(f"The grade {grade} is not valid. Please enter a number between 0 and 100.")

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
    student_list_function=[]
    
    while(another_student != "no"):
        
        full_name = input("\n Enter the student's full name: ")
        section = input("Enter the student's section: ")
        
        spanish_grade = get_valid_grade("Spanish")
        english_grade = get_valid_grade("English")
        social_studies_grade = get_valid_grade("Social Studies")
        science_grade = get_valid_grade("Science")

        student_average_grade = (spanish_grade+english_grade+social_studies_grade+science_grade)/4
        
        student = Student(student_average_grade,full_name,section,spanish_grade,english_grade,social_studies_grade,science_grade)
        
        student_list_function.append(student)
        
        another_student = input("Do you want to add another student? (yes/no): ").lower()
    
    return student_list_function

def show_registered_students(student_list):
    
    for student in student_list:
        print(f"Student name: {student.name}\n")
        print(f"Section: {student.section}\n")
        print(f"Average: {student.average}\n")
        print("Grades by subject:\n")
        
        print(f"\tSpanish: {student.spanish}\n")
        print(f"\tEnglish: {student.english}\n")
        print(f"\tSocial Studies: {student.social_studies}\n")
        print(f"\tScience: {student.science}\n")
        
        print(" --------------- * --------------- \n")

def get_top_three_students(student_list):
              
    sorted_students = sorted(student_list, key=lambda student: student.average, reverse=True)
    
    print("+++++++ TOP 3 STUDENTS BY AVERAGE GRADE +++++++ \n")

    for index in range(min(3, len(sorted_students))):
        student = sorted_students[index]
        print(f"#{index+1} {student.name}: {student.average}\n")

def get_general_average(student_list):
    
    try:
        
        total_average_sum = 0

        student_count = len(student_list)

        for student in student_list:
            total_average_sum += student.average

        general_average = round(total_average_sum / student_count, 2)

        print(f"\nThe general average is: {general_average}\n")

        
    except ZeroDivisionError as e:
            print(f"\n You tried to divide by zero. Details: {e} \n")