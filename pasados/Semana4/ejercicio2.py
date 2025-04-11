#Cree un programa que le pida al usuario su nombre, apellido, y edad, 
# y muestre si es un bebé, niño, preadolescente, adolescente, adulto joven, adulto, o adulto mayor

age = int(input("Ingrese su edad: "))
name = input("Ingrese su nombre: ")
last_name = input("Ingrese su apelido: ")
category = ""

if(age >= 0 and age <= 2):
    category = "Bebé"
elif(age >= 3 and age <= 10):
    category = "Niño"
elif(age >= 11 and age <= 13):
    category = "Preadolescente"
elif(age >= 14 and age <= 17):
    category = "Adolescente"   
elif(age >= 18 and age <= 29):
    category = "Adulto joven"
elif(age >= 30 and age <= 59):
    category = "Adulto"
elif(age >= 60):
    category = "Adulto mayor"
    
print(f" {name} {last_name}, tienes {age} años y eres {category}.")