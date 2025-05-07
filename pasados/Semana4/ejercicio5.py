#5. Dada `n` cantidad de notas de un estudiante, calcular:
    #1. Cuantas notas tiene aprobadas (mayor a 70).
    #2. Cuantas notas tiene desaprobadas (menor a 70).
    #3. El promedio de todas.
    #4. El promedio de las aprobadas.
    #5. El promedio de las desaprobadas.
    
grade_count = int(input("Ingrese el total de notas a calcular: "))

cont = 1
passing_grades = 0 
failing_grades = 0

sum_all_grades = 0
sum_passing_grades = 0
sum_failing_grades = 0

average_all_grades = 0
average_passing_grades = 0
average_failing_grades = 0

while cont <= grade_count:
    grade = float(input(f"Digite la nota {cont}: "))
    sum_all_grades += grade
    
    if(grade >=70):
        passing_grades +=1
        sum_passing_grades += grade
    else: 
        failing_grades +=1
        sum_failing_grades += grade
        
    cont+=1

average_all_grades = sum_all_grades/grade_count


if passing_grades != 0:
	average_passing_grades = sum_passing_grades/passing_grades
	
if failing_grades !=0:
	average_failing_grades = sum_failing_grades/failing_grades


print(f"El total de notas aprobadas es de: {passing_grades}")
print(f"El total de notas desaprobadas es de: {failing_grades}")

print(f"El promedio de todas las notas es de: {round(average_all_grades, 2)}")
print(f"El promedio de todas las notas aprobadas es de: {round(average_passing_grades, 2)}")
print(f"El promedio de todas las notas desaprobadas es de: {round(average_failing_grades, 2)}")