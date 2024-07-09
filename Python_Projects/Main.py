import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '39ca4d64fb56f6476b421e4e6a614b43'
HEADER = {'Content-Type' : 'application/json' , 'trainer_token' : TOKEN}
body_registration = {
     "trainer_token" : TOKEN,
     "email" : "lapunov.s@yandex.ru",
     "password" : "LS31415926"
}
body_confirmation = {
    "trainer_token" : TOKEN
}
body_create = {
    "name" : "Sauron",
    "photo_id" : 15
}

body_rename = {
    "pokemon_id": "42621",
    "name": "Golum",
    "photo_id": 3
}

add_pokeball = {
    "pokemon_id": "42621"
}

response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
print(response_create.text)

message = response_create.json()['message']
print(message)

response_rename = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_rename)
print(response_rename.text)

message = response_rename.json()['message']
print(message)

response_add_pokeball = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = add_pokeball)
print(response_add_pokeball.text)

message = response_add_pokeball.json()['message']
print(message)