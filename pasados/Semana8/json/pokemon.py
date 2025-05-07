#Ejericio 1: Cree un programa que permita agregar un Pokémon nuevo al archivo de la lección de JSON.
    # 1. Debe leer el archivo para importar los Pokémones existentes.
    # 2. Luego debe pedir la información del Pokémon a agregar.
    # 3. Finalmente debe guardar el nuevo Pokémon en el archivo.

import json

data_json = '[{"name":{"english":"Pikachu"},"type":["Electric"],"base":{"HP":35,"Attack":55,"Defense":40,"Sp. Attack":50,"Sp. Defense":50,"Speed":90}},{"name":{"english":"Charmander"},"type":["Fire"],"base":{"HP":39,"Attack":52,"Defense":43,"Sp. Attack":60,"Sp. Defense":50,"Speed":65}},{"name":{"english":"Squirtle"},"type":["Water"],"base":{"HP":44,"Attack":48,"Defense":65,"Sp. Attack":50,"Sp. Defense":64,"Speed":43}}]'

pokemon_list = json.loads(data_json)

print(pokemon_list)

name = input("Digite el nombre del pokemon")
type = input("Digite el tipo del pokemon")
hp = input("Digite el HP del pokemon")
atacck = input("Digite el ataque del pokemon")
defense = input("Digite la defensa del pokemon")
spatacck = input("Digite los SP de ataque del pokemon")
spdefense = input("Digite los SP de defensa del pokemon")
speed = input("Digite la velocidad del pokemon")

pokemon = {
    "name":{
        "english": name
    },
    "type": [
        type
    ],
    "base": {
      "HP": hp,
      "Attack": atacck,
      "Defense": defense,
      "Sp. Attack": spatacck,
      "Sp. Defense": spdefense,
      "Speed": speed
    }
}

pokemon_list.append(pokemon)

data_json = json.dumps(pokemon_list, indent=4)

print(data_json)