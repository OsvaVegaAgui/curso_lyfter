#Ejercicio1 Diccionarios: Cree un diccionario que guarde la siguiente información sobre un hotel:
#     - `nombre`
#     - `numero_de_estrellas`
#     - `habitaciones`
# - El value del key de `habitaciones` debe ser una lista, y cada habitación debe tener la siguiente información:
#     - `numero`
#     - `piso`
#     - `precio_por_noche`


nameHotel = input("Digite el nombre del hotel: ")
stars = int(input("Digite el numero de estrellas: "))

number = float(input("Digite el numero de habitacion: "))
floor = float(input("Digite el numero de piso : "))
price = float(input("Digite el precio por noche : "))

hotel = {
    'name':nameHotel,
    'stars':stars,
    'room':[
        number,
        floor,
        price
    ]
}

print(hotel)