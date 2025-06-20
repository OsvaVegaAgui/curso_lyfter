# 1. Cree una clase de `BankAccount` que:
#     1. Tenga un atributo de `balance`.
#     2. Tenga un método para ingresar dinero.
#     3. Tengo un método para retirar dinero.
    
#     Cree otra clase que herede de esta llamada `SavingsAccount` que:
    
#     1. Tenga un atributo de `min_balance` que se pueda asignar al crearla.
#     2. Arroje un error si al intentar retirar dinero, el retiro haría que el `balance` quede debajo del `min_balance`. Es decir que sí se pueden hacer retiros **siempre y cuando** el `balance` quede arriba del `min_balance`.
class InvalidMenuOption(Exception):
    def __init__(self, opc):
        super().__init__(f" \n The option {opc} is not valid. Please enter a number between 1 and 3. \n")


class BankAccount:
    balance = 5000
    
    def deposit_money(self,amount):
        self.balance += amount
    
    def withdraw_money(self,amount):
        self.balance -= amount
    
    
class SavingsAccount(BankAccount):
    def __init__(self, min_balance):
        self.min_balance = min_balance
        
    def validate_minimum_balance(self,amount):
        provisional_balance = self.balance - amount
        
        if(provisional_balance < self.min_balance):
            return False
        
        return True
                
transaction = SavingsAccount(4000)

while(True):
    
    print(f"\n Your current balance is: ${transaction.balance}")
    print("1. Add funds")        
    print("2. Remove funds")
    print("3. Exit")
    
    amount = 0
    menu_option = 0
    
    try:
    
        menu_option = int(input("Please select a menu option (1-3): "))
        
        if menu_option < 1 or menu_option > 3:
            raise InvalidMenuOption(menu_option)
        elif menu_option == 1:
            amount = int(input("Enter the amount: "))
            transaction.deposit_money(amount) 
        elif menu_option == 2:
            amount = int(input("Enter the amount: "))
            
            error = transaction.validate_minimum_balance(amount)
            
            if(error):
                transaction.withdraw_money(amount) 
            else:
                print("\n *** Withdrawal error: minimum balance reached *** \n")
            
        elif menu_option == 3:
            break
        
    except InvalidMenuOption as error:
            print(f"Error: {error}")
            
    except ValueError as error:
        print(f' \n The entered value is not a number. Please enter a valid value {error} \n')
    
    