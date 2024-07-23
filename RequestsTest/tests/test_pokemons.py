import requests
import pytest

URL = "https://api.pokemonbattle.ru/v2"
TOKEN = "796960c0d3c182f656357a1dd8873335"
HEADER = {"Content-Tape":"application/json","trainer_token": TOKEN } 
TRAINER_ID = 4041 
TRAINER_NAME = 'TOKKEN'

#Запрос get/treiners приходит с кодом 200
def test_status_code():
    response = requests.get(f'{URL}/trainers')
    assert response.status_code == 200 

def tese_trainer_name():
    response_trainers = requests.git(url = f'{URL}/trainers',params = {'trainer_id': TRAINER_ID})
    assert response_trainers.json()['data'][0]['trainer_name'] == 'Бульбазавр'