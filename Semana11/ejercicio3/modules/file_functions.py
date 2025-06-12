import csv

class Student():
    def __init__(self, average,name,section,spanish,english,social_studies,science):
        self.average = average
        self.name = name
        self.section = section
        self.spanish = spanish
        self.english = english
        self.social_studies = social_studies
        self.science = science

def export_student_data(student_list):
    
    with open('students.csv', 'w', encoding='utf-8') as file:
        fieldnames = ["average", "name", "section", "spanish", "english", "social_studies", "science"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for student in student_list:
            writer.writerow({
                "average": student.average,
                "name": student.name,
                "section": student.section,
                "spanish": student.spanish,
                "english": student.english,
                "social_studies": student.social_studies,
                "science": student.science
            })
        
    print("\n File created successfully \n")

def import_student_data():
    
    student_list_function=[]
    
    try:
    
        with open('students.csv', 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                student = Student(
                    average=float(row["average"]),
                    name=row["name"],
                    section=row["section"],
                    spanish=float(row["spanish"]),
                    english=float(row["english"]),
                    social_studies=float(row["social_studies"]),
                    science=float(row["science"])
                )
                student_list_function.append(student)
                
        print("\n File imported successfully \n")
        
        return student_list_function
        
    except FileNotFoundError:
        print("\nThe file 'students.csv' was not found. Please export data first.\n")