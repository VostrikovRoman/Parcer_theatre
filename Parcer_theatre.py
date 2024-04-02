from bs4 import BeautifulSoup
import requests
import json

url = 'https://tagildrama.ru/afisha'
page = requests.get(url)

all_posters = []
posters = []

soup = BeautifulSoup(page.text, "html.parser")
all_posters = soup.findAll('div', class_='one-poster')

Posters = {}
result =[]

for i in all_posters:
    Posters ={
        "name": i.find('h4', class_='font-title').find('a').text,
        "date": i.find('div', class_='day-month').find('h2').text + " " + i.find('div', class_='day-month').find('p').text,
        "week": i.find('div', class_='day-time').find('p').text,
        "genre": i.find('div', class_='poster-info').find('p').text,
        "age_category": i.find('div', class_='poster-info').find('p', class_='bronze-color').text[21:],
        "link": 'https://tagildrama.ru' + i.find('h4', class_='font-title').find('a').get('href')
    }
    result.append(Posters)


with open ("Posters.json", "w", encoding='utf-8') as json_file:
    json.dump(result, json_file, ensure_ascii=False, indent=4)

poster = json.dumps(Posters)


