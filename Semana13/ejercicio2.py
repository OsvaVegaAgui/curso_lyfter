# Cree un decorador que se encargue de revisar si todos los parámetros de la función 
# que decore son números, y arroje una excepción de no ser así.

def validate_numbers(func):
    def wrapper(*args, **kwargs):
        for num in args:
            if not isinstance(num, (int, float)):
                raise ValueError(f'The entered value is not a number: {num}.')
            
        for key, value in kwargs.items():
            if not isinstance(value, (int, float)):
                raise ValueError(f'The entered value for "{key}" is not a number: {value}.')
        return func(*args, **kwargs)
    return wrapper

@validate_numbers
def get_numbers(num1=0, num2=0, num3=0, num4=0):
    return num1 + num2

try:
    print(get_numbers(7,'nueve'))
except ValueError as error:
    print(f'Error: {error}')
