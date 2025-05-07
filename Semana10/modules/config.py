student_list = []

class InvalidMenuOption(Exception):
    def __init__(self, opc):
        super().__init__(f"The option {opc} is not valid. Please enter a number between 1 and 7.")
        
class InvalidGrade(Exception):
    def __init__(self, grade):
        super().__init__(f"The grade {grade} is not valid. Please enter a number between 0 and 100.")
