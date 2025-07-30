# 3. Cree una clase de `User` que:
#     - Tenga un atributo de `date_of_birth`.
#     - Tenga un property de `age`.
    
#     Luego cree un decorador para funciones que acepten un `User` como parámetro 
#     que se encargue de revisar si el `User` es mayor de edad y 
#     arroje una excepción de no ser así.

from datetime import date,datetime

class User:
    def __init__(self, date_of_birth):
        self.date_of_birth = date_of_birth

    @property
    def age(self):
        current_day = date.today()
        age = current_day.year - self.date_of_birth.year

        if (current_day.month, current_day.day) < (self.date_of_birth.month, self.date_of_birth.day):
            age -= 1
        return age

def legal_age(func):
    def wrapper(user, *args):
        if user.age < 18:
            raise ValueError('They are not of legal age.')
        return func(user, *args)
    return wrapper

@legal_age
def  get_permission(user):
    return 'The user is of legal age.'

user = User(datetime(2015, 11, 23))

try:
    print(get_permission(user))
except ValueError as error:
    print(f'Error: {error}')
