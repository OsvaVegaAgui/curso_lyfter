import csv

def export_student_data(student_list):
    
    with open('students.csv', 'w', encoding='utf-8') as file:
        writer = csv.DictWriter(file, student_list[0].keys())
        writer.writeheader()
        writer.writerows(student_list)
        
    print("\n File created successfully \n")

def import_student_data():
    
    student_list_function=[]
    
    try:
    
        with open('students.csv', 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                student = {
                    "average": float(row["average"]),
                    "name": row["name"],
                    "section": row["section"],
                    "spanish": float(row["spanish"]),
                    "english": float(row["english"]),
                    "social_studies": float(row["social_studies"]),
                    "science": float(row["science"])
                }
                student_list_function.append(student)
                
        print("\n File imported successfully \n")
        
        return student_list_function
        
    except FileNotFoundError:
        print("\nThe file 'students.csv' was not found. Please export data first.\n")