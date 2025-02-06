import requests as req
import json
import arrow
from geopy.geocoders import Nominatim

#Função para registrar o endereço e retornar a latitude e longitude
def get_location(address):
    geolocator = Nominatim(user_agent="geoapi")
    location = geolocator.geocode(address)

    return location.latitude, location.longitude

#Pegando o endereço do usuário
loc = input("Informe o endereço desejado: ")

#Pegando a latitude e longitude usando a função
latitude, longitude = get_location(loc)

#Crie um arquivo chamado hash_api.txt e coloque a chave da API dentro dele
file = open('weather_hash_api.txt', 'r')

#Lendo o arquivo
content = file.read()

# Pegar a primeira hora do dia
start = arrow.now().floor('day')

# Pegar a última hora do dia
end = arrow.now().ceil('day')

#Fazendo a requisição
response = req.get(
    'https://api.stormglass.io/v2/weather/point',
    params={
        'lat': latitude, 
        'lng': longitude,
        'params': 'airTemperature,cloudCover',
        'start': start.to('UTC').timestamp(),
        'end': end.to('UTC').timestamp() 
    },
    headers={'Authorization': content}
)

#Transformando em JSON
json_data = response.json()

#Printando o JSON com os resultados
print(json_data)

#Fechando o arquivo
file.close()

