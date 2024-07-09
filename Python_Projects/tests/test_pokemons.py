import requests
import pytest
URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '39ca4d64fb56f6476b421e4e6a614b43'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}
TRAINER_ID = '4237'

def test_status_code():
    response = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : TRAINER_ID})
    assert response.status_code == 200

def test_part_of_response():
    response_get = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : TRAINER_ID})
    assert response_get.json()["data"][0]["trainer_name"] == "Maverick"