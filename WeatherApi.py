import requests as req
import json as js
import arrow


#Crie um arquivo chamado hash_api.txt e coloque a chave da API dentro dele
file = open('hash_api.txt', 'r')

#Lendo o arquivo
content = file.read()

# Pegar a primeira hora do dia
start = arrow.now().floor('day')

# Pegar a última hora do dia
end = arrow.now().ceil('day')

latitude = input("Digite a Latitude e Longitude separadas por ponto e vírgula: ")

longitude = latitude.split(";")

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

file.close()

