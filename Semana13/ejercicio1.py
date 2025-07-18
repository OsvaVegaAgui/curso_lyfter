# Cree un decorador que haga print de los parámetros y retorno de la función que decore.

def print_and_return(func):
    def wrapper(marriage_year, current_year):
        print(f"Printing parameters: {marriage_year} and {current_year}")
        result = func(marriage_year, current_year)
        print(f"Printing result: {result}")
    return wrapper

@print_and_return
def get_years_married(marriage_year, current_year):
    return current_year - marriage_year

get_years_married(2015, 2025)

