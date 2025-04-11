#Ejercicio 5: Cree una función que imprima el numero de mayúsculas y el numero de minúsculas en un string

uppercase_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
lowercase_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ','o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def print_letters(sentence):
    total_uppercase=0
    total_lowercase=0
    
    for index in range(0,len(sentence)):
        letter = sentence[index]
        for index2 in range(0,len(uppercase_letters)):
            if(letter == uppercase_letters[index2]):
                total_uppercase +=1
            elif (letter == lowercase_letters[index2]):
                total_lowercase +=1
    
    return f"En el texto {sentence} hay: {total_uppercase} mayúsculas y {total_lowercase} minúsculas"
    
print(print_letters("OSVALDO VEGA"))
print(print_letters("osvaldo vega"))
print(print_letters("Osvaldo Vega"))