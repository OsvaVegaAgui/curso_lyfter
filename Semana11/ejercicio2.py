# 2. Cree una clase de `Bus` con:
#     1. Un atributo de `max_passengers`.
#     2. Un método para agregar pasajeros uno por uno (que acepte como parámetro una instancia de la clase `Person` vista en la lección). **Este solo debe agregar pasajeros si lleva menos de su máximo.** Sino, debe mostrar un mensaje de que el bus está lleno.
#     3. Un método para bajar pasajeros uno por uno (en cualquier orden).

class InvalidMenuOption(Exception):
    def __init__(self, opc):
        super().__init__(f" \n The option {opc} is not valid. Please enter a number between 1 and 3. \n")

class Person():
    def __init__(self, name,age,id):
        self.passenger = {'id':id,'name':name,'age':age}

class Bus:
    max_passengers = 2
    passenger_list = []
    
    def add_passenger(self,passenger):
        
        if(len(self.passenger_list) >= self.max_passengers):
            print("\n ^^^^^^ The bus is full. ^^^^^^\n")
        else:
            self.passenger_list.append(passenger)
            print("\n ****** Passenger successfully added. *******\n")
            
def get_passenger_data():
    name = input("Enter the person's name: ")
    age = int(input("Enter the person's age: "))
    id = int(input("Enter the person's ID: "))

    person = Person(name,age,id)
    passenger = person.passenger
    
    bus = Bus()
    bus.add_passenger(passenger)
    
def remove_passenger():
    bus = Bus()
                
    print("\n")
    
    for passenger in bus.passenger_list:
        
        print(f"ID: {passenger['id']} / Name: {passenger['name']} / Age: {passenger['age']}")
        
    print("\n")
    
    id= int(input("Enter the passenger's ID to get off the bus:"))
    
    passenger_found = False
    
    for index in range(0,len(bus.passenger_list)):
        
        if(bus.passenger_list[index]["id"] == id):
            bus.passenger_list.pop(index)
            print("\n **** Passenger removed from the bus **** \n")
            passenger_found = True
            break
        
    if(not passenger_found):
        print("\n ^^^^ Passenger not found ^^^^ \n")

def main():
    
    while(True):
        try:
            print("1. Add passenger")
            print("2. Remove passenger")
            print("3. Exit")
            menu_option = int(input("Please select a menu option (1-3): "))
            
            if menu_option < 1 or menu_option > 7:
                raise InvalidMenuOption(menu_option)
            elif menu_option == 1:
                get_passenger_data()
            elif menu_option == 2:
                remove_passenger()
            
        except InvalidMenuOption as error:
                print(f"Error: {error}")
                
        except ValueError as error:
            print(f' \n The entered value is not a number. Please enter a valid value {error} \n')

main()