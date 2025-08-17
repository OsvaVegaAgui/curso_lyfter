#Ejercicio 6: Cree una función que acepte un string con palabras separadas por un guión y retorne un string igual pero ordenado alfabéticamente.

def get_text(sentence):
    list_words = sentence.split("-")
    list_order = sorted(list_words)
    
    text = list_order[0]
    
    for index in range(1, len(list_order)):
        text = text + "-" + list_order[index]
    
    return text
    
result = get_text("python-variable-funcion-computadora-monitor")