

```python
# Dependencies
import csv
import pandas as pd
import matplotlib.pyplot as plt
import json
import requests as req
from citipy import citipy
import random

```


```python
# Some random coordinates
coordinates = []
count = 0
while count != 550:
    count += 1
    tuple_for_list=  (random.randint(0,50),(random.randint(0,200)))
    coordinates.append(tuple_for_list)
#coordinates
#len(coordinates)

cities = []
cities_detail = []
for coordinate_pair in coordinates:
    lat, lon = coordinate_pair
    cities_detail.append(citipy.nearest_city(lat, lon))
#print (cities_detail)

for city in cities_detail:
    #country_code = city.country_code
    name = city.city_name
    #print("The country code of " + name + " is '" + country_code + "'.")
    cities.append(name)
#print (len(cities))
```


```python
# Save config information
#api_key = "25bc90a1196e6f153eece0bc0b0fc9eb"
api_key = "7be7dfb02672af49d73e9ca689405225"
url = "http://api.openweathermap.org/data/2.5/weather?"
units = "metric"

# Build partial query URL
query_url = url + "appid=" + api_key + "&units=" + units + "&q="
```


```python
#Creating a big list with all the infor for all the cites and getting the response for JSON
weather_data_list = []

# Loop through the list of cities and perform a request for data on each
city_count = 0
for city in cities:
    weather_response_json = req.get(query_url + city).json()
    weather_data_list.append(weather_response_json)
    city_count += 1
    print ("Processing Record:",city_count, "of 550", "| city: ",city, "\n", query_url + city)
```

    Processing Record: 1 of 550 | city:  aden 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=aden
    Processing Record: 2 of 550 | city:  beringovskiy 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=beringovskiy
    Processing Record: 3 of 550 | city:  kulhudhuffushi 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=kulhudhuffushi
    Processing Record: 4 of 550 | city:  severo-kurilsk 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=severo-kurilsk
    Processing Record: 5 of 550 | city:  zaysan 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=zaysan
    Processing Record: 6 of 550 | city:  shache 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=shache
    Processing Record: 7 of 550 | city:  nalgonda 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=nalgonda
    Processing Record: 8 of 550 | city:  tidore 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=tidore
    Processing Record: 9 of 550 | city:  butaritari 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=butaritari
    Processing Record: 10 of 550 | city:  rungata 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=rungata
    Processing Record: 11 of 550 | city:  severo-kurilsk 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=severo-kurilsk
    Processing Record: 12 of 550 | city:  urumqi 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=urumqi
    Processing Record: 13 of 550 | city:  meulaboh 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=meulaboh
    Processing Record: 14 of 550 | city:  sayyan 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=sayyan
    Processing Record: 15 of 550 | city:  kutum 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=kutum
    Processing Record: 16 of 550 | city:  tripoli 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=tripoli
    Processing Record: 17 of 550 | city:  rungata 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=rungata
    Processing Record: 18 of 550 | city:  sabha 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=sabha
    Processing Record: 19 of 550 | city:  jumla 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=jumla
    Processing Record: 20 of 550 | city:  shimoda 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=shimoda
    Processing Record: 21 of 550 | city:  airai 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=airai
    Processing Record: 22 of 550 | city:  korla 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=korla
    Processing Record: 23 of 550 | city:  bandarbeyla 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=bandarbeyla
    Processing Record: 24 of 550 | city:  blensong 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=blensong
    Processing Record: 25 of 550 | city:  marawi 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=marawi
    Processing Record: 26 of 550 | city:  altay 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=altay
    Processing Record: 27 of 550 | city:  longhua 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=longhua
    Processing Record: 28 of 550 | city:  butaritari 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=butaritari
    Processing Record: 29 of 550 | city:  kollam 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=kollam
    Processing Record: 30 of 550 | city:  sasaram 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=sasaram
    Processing Record: 31 of 550 | city:  beringovskiy 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=beringovskiy
    Processing Record: 32 of 550 | city:  nishihara 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=nishihara
    Processing Record: 33 of 550 | city:  maebaru 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=maebaru
    Processing Record: 34 of 550 | city:  airai 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=airai
    Processing Record: 35 of 550 | city:  vanimo 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=vanimo
    Processing Record: 36 of 550 | city:  linqiong 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=linqiong
    Processing Record: 37 of 550 | city:  bilma 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=bilma
    Processing Record: 38 of 550 | city:  butaritari 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=butaritari
    Processing Record: 39 of 550 | city:  carikar 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=carikar
    Processing Record: 40 of 550 | city:  tchollire 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=tchollire
    Processing Record: 41 of 550 | city:  rungata 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=rungata
    Processing Record: 42 of 550 | city:  galle 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=galle
    Processing Record: 43 of 550 | city:  arlit 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=arlit
    Processing Record: 44 of 550 | city:  qandala 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=qandala
    Processing Record: 45 of 550 | city:  nikolskoye 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=nikolskoye
    Processing Record: 46 of 550 | city:  baringo 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=baringo
    Processing Record: 47 of 550 | city:  novikovo 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=novikovo
    Processing Record: 48 of 550 | city:  phan rang 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=phan rang
    Processing Record: 49 of 550 | city:  miri 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=miri
    Processing Record: 50 of 550 | city:  carbonia 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=carbonia
    Processing Record: 51 of 550 | city:  kapit 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=kapit
    Processing Record: 52 of 550 | city:  tezu 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=tezu
    Processing Record: 53 of 550 | city:  anakapalle 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=anakapalle
    Processing Record: 54 of 550 | city:  khangarh 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=khangarh
    Processing Record: 55 of 550 | city:  lar gerd 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=lar gerd
    Processing Record: 56 of 550 | city:  aksu 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=aksu
    Processing Record: 57 of 550 | city:  bushehr 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=bushehr
    Processing Record: 58 of 550 | city:  petropavlovsk-kamchatskiy 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=petropavlovsk-kamchatskiy
    Processing Record: 59 of 550 | city:  butaritari 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=butaritari
    Processing Record: 60 of 550 | city:  beringovskiy 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=beringovskiy
    Processing Record: 61 of 550 | city:  port blair 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=port blair
    Processing Record: 62 of 550 | city:  marawi 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=marawi
    Processing Record: 63 of 550 | city:  beringovskiy 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=beringovskiy
    Processing Record: 64 of 550 | city:  butaritari 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=butaritari
    Processing Record: 65 of 550 | city:  kloulklubed 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=kloulklubed
    Processing Record: 66 of 550 | city:  anshun 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=anshun
    Processing Record: 67 of 550 | city:  butaritari 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=butaritari
    Processing Record: 68 of 550 | city:  balabac 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=balabac
    Processing Record: 69 of 550 | city:  kon tum 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=kon tum
    Processing Record: 70 of 550 | city:  hami 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=hami
    Processing Record: 71 of 550 | city:  hami 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=hami
    Processing Record: 72 of 550 | city:  labuan 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=labuan
    Processing Record: 73 of 550 | city:  baijiantan 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=baijiantan
    Processing Record: 74 of 550 | city:  fasa 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=fasa
    Processing Record: 75 of 550 | city:  lorengau 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=lorengau
    Processing Record: 76 of 550 | city:  xining 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=xining
    Processing Record: 77 of 550 | city:  banyo 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=banyo
    Processing Record: 78 of 550 | city:  sentyabrskiy 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=sentyabrskiy
    Processing Record: 79 of 550 | city:  yangmei 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=yangmei
    Processing Record: 80 of 550 | city:  hovd 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=hovd
    Processing Record: 81 of 550 | city:  kuroiso 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=kuroiso
    Processing Record: 82 of 550 | city:  sur 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=sur
    Processing Record: 83 of 550 | city:  epe 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=epe
    Processing Record: 84 of 550 | city:  salalah 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=salalah
    Processing Record: 85 of 550 | city:  jimma 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=jimma
    Processing Record: 86 of 550 | city:  nikolskoye 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=nikolskoye
    Processing Record: 87 of 550 | city:  marawi 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=marawi
    Processing Record: 88 of 550 | city:  marawi 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=marawi
    Processing Record: 89 of 550 | city:  kattivakkam 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=kattivakkam
    Processing Record: 90 of 550 | city:  butaritari 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=butaritari
    Processing Record: 91 of 550 | city:  pathein 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=pathein
    Processing Record: 92 of 550 | city:  aleppo 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=aleppo
    Processing Record: 93 of 550 | city:  kuryk 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=kuryk
    Processing Record: 94 of 550 | city:  hargeysa 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=hargeysa
    Processing Record: 95 of 550 | city:  airai 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=airai
    Processing Record: 96 of 550 | city:  terme 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=terme
    Processing Record: 97 of 550 | city:  gushikawa 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=gushikawa
    Processing Record: 98 of 550 | city:  phan thiet 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=phan thiet
    Processing Record: 99 of 550 | city:  airai 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=airai
    Processing Record: 100 of 550 | city:  delijan 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=delijan
    Processing Record: 101 of 550 | city:  panjab 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=panjab
    Processing Record: 102 of 550 | city:  savantvadi 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=savantvadi
    Processing Record: 103 of 550 | city:  susurluk 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=susurluk
    Processing Record: 104 of 550 | city:  rungata 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=rungata
    Processing Record: 105 of 550 | city:  maiduguri 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=maiduguri
    Processing Record: 106 of 550 | city:  uthal 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=uthal
    Processing Record: 107 of 550 | city:  namatanai 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=namatanai
    Processing Record: 108 of 550 | city:  butaritari 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=butaritari
    Processing Record: 109 of 550 | city:  beringovskiy 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=beringovskiy
    Processing Record: 110 of 550 | city:  victoria 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=victoria
    Processing Record: 111 of 550 | city:  udankudi 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=udankudi
    Processing Record: 112 of 550 | city:  manzhouli 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=manzhouli
    Processing Record: 113 of 550 | city:  hit 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=hit
    Processing Record: 114 of 550 | city:  rungata 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=rungata
    Processing Record: 115 of 550 | city:  brcko 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=brcko
    Processing Record: 116 of 550 | city:  nemuro 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=nemuro
    Processing Record: 117 of 550 | city:  bam 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=bam
    Processing Record: 118 of 550 | city:  kulevcha 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=kulevcha
    Processing Record: 119 of 550 | city:  butaritari 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=butaritari
    Processing Record: 120 of 550 | city:  mahon 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=mahon
    Processing Record: 121 of 550 | city:  wadi musa 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=wadi musa
    Processing Record: 122 of 550 | city:  seoul 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=seoul
    Processing Record: 123 of 550 | city:  korla 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=korla
    Processing Record: 124 of 550 | city:  pemangkat 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=pemangkat
    Processing Record: 125 of 550 | city:  dauriya 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=dauriya
    Processing Record: 126 of 550 | city:  fukue 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=fukue
    Processing Record: 127 of 550 | city:  meulaboh 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=meulaboh
    Processing Record: 128 of 550 | city:  lorengau 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=lorengau
    Processing Record: 129 of 550 | city:  hasaki 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=hasaki
    Processing Record: 130 of 550 | city:  mahasamund 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=mahasamund
    Processing Record: 131 of 550 | city:  rungata 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=rungata
    Processing Record: 132 of 550 | city:  wadi musa 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=wadi musa
    Processing Record: 133 of 550 | city:  sur 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=sur
    Processing Record: 134 of 550 | city:  si sa ket 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=si sa ket
    Processing Record: 135 of 550 | city:  beringovskiy 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=beringovskiy
    Processing Record: 136 of 550 | city:  det udom 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=det udom
    Processing Record: 137 of 550 | city:  victoria 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=victoria
    Processing Record: 138 of 550 | city:  butaritari 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=butaritari
    Processing Record: 139 of 550 | city:  oyama 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=oyama
    Processing Record: 140 of 550 | city:  butaritari 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=butaritari
    Processing Record: 141 of 550 | city:  nawa 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=nawa
    Processing Record: 142 of 550 | city:  seoul 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=seoul
    Processing Record: 143 of 550 | city:  faya 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=faya
    Processing Record: 144 of 550 | city:  tonj 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=tonj
    Processing Record: 145 of 550 | city:  panzhihua 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=panzhihua
    Processing Record: 146 of 550 | city:  salalah 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=salalah
    Processing Record: 147 of 550 | city:  katsuura 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=katsuura
    Processing Record: 148 of 550 | city:  sentyabrskiy 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=sentyabrskiy
    Processing Record: 149 of 550 | city:  fukue 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=fukue
    Processing Record: 150 of 550 | city:  butaritari 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=butaritari
    Processing Record: 151 of 550 | city:  kantang 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=kantang
    Processing Record: 152 of 550 | city:  payo 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=payo
    Processing Record: 153 of 550 | city:  yumen 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=yumen
    Processing Record: 154 of 550 | city:  mogadishu 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=mogadishu
    Processing Record: 155 of 550 | city:  butaritari 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=butaritari
    Processing Record: 156 of 550 | city:  marawi 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=marawi
    Processing Record: 157 of 550 | city:  leh 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=leh
    Processing Record: 158 of 550 | city:  ohara 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=ohara
    Processing Record: 159 of 550 | city:  turayf 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=turayf
    Processing Record: 160 of 550 | city:  gushikawa 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=gushikawa
    Processing Record: 161 of 550 | city:  manavalakurichi 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=manavalakurichi
    Processing Record: 162 of 550 | city:  kushima 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=kushima
    Processing Record: 163 of 550 | city:  viramgam 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=viramgam
    Processing Record: 164 of 550 | city:  staryy saltiv 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=staryy saltiv
    Processing Record: 165 of 550 | city:  butaritari 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=butaritari
    Processing Record: 166 of 550 | city:  nikki 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=nikki
    Processing Record: 167 of 550 | city:  salalah 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=salalah
    Processing Record: 168 of 550 | city:  butaritari 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=butaritari
    Processing Record: 169 of 550 | city:  kargil 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=kargil
    Processing Record: 170 of 550 | city:  shaoguan 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=shaoguan
    Processing Record: 171 of 550 | city:  hazorasp 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=hazorasp
    Processing Record: 172 of 550 | city:  nikolskoye 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=nikolskoye
    Processing Record: 173 of 550 | city:  rawannawi 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=rawannawi
    Processing Record: 174 of 550 | city:  warqla 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=warqla
    Processing Record: 175 of 550 | city:  kirovskiy 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=kirovskiy
    Processing Record: 176 of 550 | city:  locri 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=locri
    Processing Record: 177 of 550 | city:  dunhua 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=dunhua
    Processing Record: 178 of 550 | city:  kungurtug 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=kungurtug
    Processing Record: 179 of 550 | city:  ajdabiya 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=ajdabiya
    Processing Record: 180 of 550 | city:  punalur 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=punalur
    Processing Record: 181 of 550 | city:  rungata 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=rungata
    Processing Record: 182 of 550 | city:  djougou 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=djougou
    Processing Record: 183 of 550 | city:  butaritari 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=butaritari
    Processing Record: 184 of 550 | city:  ishigaki 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=ishigaki
    Processing Record: 185 of 550 | city:  zhanaozen 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=zhanaozen
    Processing Record: 186 of 550 | city:  payo 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=payo
    Processing Record: 187 of 550 | city:  yumen 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=yumen
    Processing Record: 188 of 550 | city:  shimoda 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=shimoda
    Processing Record: 189 of 550 | city:  trabzon 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=trabzon
    Processing Record: 190 of 550 | city:  abha 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=abha
    Processing Record: 191 of 550 | city:  beringovskiy 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=beringovskiy
    Processing Record: 192 of 550 | city:  gazojak 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=gazojak
    Processing Record: 193 of 550 | city:  rungata 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=rungata
    Processing Record: 194 of 550 | city:  rungata 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=rungata
    Processing Record: 195 of 550 | city:  teseney 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=teseney
    Processing Record: 196 of 550 | city:  butaritari 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=butaritari
    Processing Record: 197 of 550 | city:  salalah 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=salalah
    Processing Record: 198 of 550 | city:  mega 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=mega
    Processing Record: 199 of 550 | city:  butaritari 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=butaritari
    Processing Record: 200 of 550 | city:  bogande 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=bogande
    Processing Record: 201 of 550 | city:  lakhisarai 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=lakhisarai
    Processing Record: 202 of 550 | city:  terney 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=terney
    Processing Record: 203 of 550 | city:  xichang 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=xichang
    Processing Record: 204 of 550 | city:  enshi 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=enshi
    Processing Record: 205 of 550 | city:  chunian 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=chunian
    Processing Record: 206 of 550 | city:  san policarpo 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=san policarpo
    Processing Record: 207 of 550 | city:  najran 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=najran
    Processing Record: 208 of 550 | city:  severo-kurilsk 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=severo-kurilsk
    Processing Record: 209 of 550 | city:  sevlievo 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=sevlievo
    Processing Record: 210 of 550 | city:  butaritari 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=butaritari
    Processing Record: 211 of 550 | city:  gigmoto 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=gigmoto
    Processing Record: 212 of 550 | city:  staryy saltiv 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=staryy saltiv
    Processing Record: 213 of 550 | city:  butaritari 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=butaritari
    Processing Record: 214 of 550 | city:  nikolskoye 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=nikolskoye
    Processing Record: 215 of 550 | city:  balabac 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=balabac
    Processing Record: 216 of 550 | city:  asau 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=asau
    Processing Record: 217 of 550 | city:  cambrils 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=cambrils
    Processing Record: 218 of 550 | city:  butaritari 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=butaritari
    Processing Record: 219 of 550 | city:  atasu 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=atasu
    Processing Record: 220 of 550 | city:  nikolskoye 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=nikolskoye
    Processing Record: 221 of 550 | city:  korla 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=korla
    Processing Record: 222 of 550 | city:  rungata 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=rungata
    Processing Record: 223 of 550 | city:  yashan 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=yashan
    Processing Record: 224 of 550 | city:  kathmandu 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=kathmandu
    Processing Record: 225 of 550 | city:  dubai 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=dubai
    Processing Record: 226 of 550 | city:  butaritari 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=butaritari
    Processing Record: 227 of 550 | city:  victoria 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=victoria
    Processing Record: 228 of 550 | city:  syedove 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=syedove
    Processing Record: 229 of 550 | city:  nikolskoye 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=nikolskoye
    Processing Record: 230 of 550 | city:  ron phibun 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=ron phibun
    Processing Record: 231 of 550 | city:  shitanjing 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=shitanjing
    Processing Record: 232 of 550 | city:  da lat 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=da lat
    Processing Record: 233 of 550 | city:  rungata 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=rungata
    Processing Record: 234 of 550 | city:  gurgan 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=gurgan
    Processing Record: 235 of 550 | city:  butaritari 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=butaritari
    Processing Record: 236 of 550 | city:  pokhara 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=pokhara
    Processing Record: 237 of 550 | city:  lorengau 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=lorengau
    Processing Record: 238 of 550 | city:  maloh 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=maloh
    Processing Record: 239 of 550 | city:  katsuura 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=katsuura
    Processing Record: 240 of 550 | city:  airai 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=airai
    Processing Record: 241 of 550 | city:  ellwangen 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=ellwangen
    Processing Record: 242 of 550 | city:  butaritari 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=butaritari
    Processing Record: 243 of 550 | city:  alaca 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=alaca
    Processing Record: 244 of 550 | city:  beringovskiy 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=beringovskiy
    Processing Record: 245 of 550 | city:  karauzyak 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=karauzyak
    Processing Record: 246 of 550 | city:  hailin 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=hailin
    Processing Record: 247 of 550 | city:  ondorhaan 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=ondorhaan
    Processing Record: 248 of 550 | city:  nakhon ratchasima 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=nakhon ratchasima
    Processing Record: 249 of 550 | city:  jinchang 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=jinchang
    Processing Record: 250 of 550 | city:  erdemli 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=erdemli
    Processing Record: 251 of 550 | city:  beringovskiy 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=beringovskiy
    Processing Record: 252 of 550 | city:  jumla 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=jumla
    Processing Record: 253 of 550 | city:  karkaralinsk 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=karkaralinsk
    Processing Record: 254 of 550 | city:  uthal 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=uthal
    Processing Record: 255 of 550 | city:  butaritari 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=butaritari
    Processing Record: 256 of 550 | city:  akyab 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=akyab
    Processing Record: 257 of 550 | city:  rungata 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=rungata
    Processing Record: 258 of 550 | city:  nikolskoye 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=nikolskoye
    Processing Record: 259 of 550 | city:  amurzet 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=amurzet
    Processing Record: 260 of 550 | city:  smidovich 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=smidovich
    Processing Record: 261 of 550 | city:  temaraia 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=temaraia
    Processing Record: 262 of 550 | city:  mujiayingzi 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=mujiayingzi
    Processing Record: 263 of 550 | city:  jalu 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=jalu
    Processing Record: 264 of 550 | city:  airai 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=airai
    Processing Record: 265 of 550 | city:  priargunsk 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=priargunsk
    Processing Record: 266 of 550 | city:  timbangan 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=timbangan
    Processing Record: 267 of 550 | city:  faya 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=faya
    Processing Record: 268 of 550 | city:  najran 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=najran
    Processing Record: 269 of 550 | city:  butaritari 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=butaritari
    Processing Record: 270 of 550 | city:  hasaki 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=hasaki
    Processing Record: 271 of 550 | city:  zhmerynka 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=zhmerynka
    Processing Record: 272 of 550 | city:  tabas 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=tabas
    Processing Record: 273 of 550 | city:  abha 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=abha
    Processing Record: 274 of 550 | city:  petropavlovsk-kamchatskiy 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=petropavlovsk-kamchatskiy
    Processing Record: 275 of 550 | city:  gayeri 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=gayeri
    Processing Record: 276 of 550 | city:  mathbaria 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=mathbaria
    Processing Record: 277 of 550 | city:  shirak 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=shirak
    Processing Record: 278 of 550 | city:  qandala 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=qandala
    Processing Record: 279 of 550 | city:  meyungs 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=meyungs
    Processing Record: 280 of 550 | city:  khor 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=khor
    Processing Record: 281 of 550 | city:  shache 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=shache
    Processing Record: 282 of 550 | city:  katsiveli 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=katsiveli
    Processing Record: 283 of 550 | city:  bayog 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=bayog
    Processing Record: 284 of 550 | city:  olga 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=olga
    Processing Record: 285 of 550 | city:  aneho 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=aneho
    Processing Record: 286 of 550 | city:  bandarbeyla 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=bandarbeyla
    Processing Record: 287 of 550 | city:  ulaanbaatar 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=ulaanbaatar
    Processing Record: 288 of 550 | city:  nikolskoye 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=nikolskoye
    Processing Record: 289 of 550 | city:  rungata 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=rungata
    Processing Record: 290 of 550 | city:  gofitskoye 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=gofitskoye
    Processing Record: 291 of 550 | city:  isiro 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=isiro
    Processing Record: 292 of 550 | city:  sentyabrskiy 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=sentyabrskiy
    Processing Record: 293 of 550 | city:  salalah 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=salalah
    Processing Record: 294 of 550 | city:  butaritari 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=butaritari
    Processing Record: 295 of 550 | city:  veraval 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=veraval
    Processing Record: 296 of 550 | city:  hasaki 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=hasaki
    Processing Record: 297 of 550 | city:  kapoeta 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=kapoeta
    Processing Record: 298 of 550 | city:  can 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=can
    Processing Record: 299 of 550 | city:  nikolskoye 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=nikolskoye
    Processing Record: 300 of 550 | city:  mandapam 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=mandapam
    Processing Record: 301 of 550 | city:  riyadh 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=riyadh
    Processing Record: 302 of 550 | city:  kloulklubed 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=kloulklubed
    Processing Record: 303 of 550 | city:  barbar 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=barbar
    Processing Record: 304 of 550 | city:  arlit 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=arlit
    Processing Record: 305 of 550 | city:  nishihara 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=nishihara
    Processing Record: 306 of 550 | city:  tessalit 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=tessalit
    Processing Record: 307 of 550 | city:  bati 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=bati
    Processing Record: 308 of 550 | city:  severo-kurilsk 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=severo-kurilsk
    Processing Record: 309 of 550 | city:  palaikastron 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=palaikastron
    Processing Record: 310 of 550 | city:  anito 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=anito
    Processing Record: 311 of 550 | city:  dourbali 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=dourbali
    Processing Record: 312 of 550 | city:  korla 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=korla
    Processing Record: 313 of 550 | city:  beringovskiy 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=beringovskiy
    Processing Record: 314 of 550 | city:  khanu woralaksaburi 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=khanu woralaksaburi
    Processing Record: 315 of 550 | city:  zharkent 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=zharkent
    Processing Record: 316 of 550 | city:  baghdad 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=baghdad
    Processing Record: 317 of 550 | city:  tiruvottiyur 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=tiruvottiyur
    Processing Record: 318 of 550 | city:  butaritari 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=butaritari
    Processing Record: 319 of 550 | city:  ellwangen 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=ellwangen
    Processing Record: 320 of 550 | city:  rungata 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=rungata
    Processing Record: 321 of 550 | city:  shimoda 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=shimoda
    Processing Record: 322 of 550 | city:  srivardhan 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=srivardhan
    Processing Record: 323 of 550 | city:  nemuro 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=nemuro
    Processing Record: 324 of 550 | city:  butaritari 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=butaritari
    Processing Record: 325 of 550 | city:  butaritari 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=butaritari
    Processing Record: 326 of 550 | city:  trapani 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=trapani
    Processing Record: 327 of 550 | city:  sholavandan 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=sholavandan
    Processing Record: 328 of 550 | city:  butaritari 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=butaritari
    Processing Record: 329 of 550 | city:  beringovskiy 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=beringovskiy
    Processing Record: 330 of 550 | city:  harmanli 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=harmanli
    Processing Record: 331 of 550 | city:  kloulklubed 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=kloulklubed
    Processing Record: 332 of 550 | city:  najran 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=najran
    Processing Record: 333 of 550 | city:  gardan diwal 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=gardan diwal
    Processing Record: 334 of 550 | city:  voskevan 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=voskevan
    Processing Record: 335 of 550 | city:  benicarlo 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=benicarlo
    Processing Record: 336 of 550 | city:  taixing 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=taixing
    Processing Record: 337 of 550 | city:  yatou 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=yatou
    Processing Record: 338 of 550 | city:  butaritari 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=butaritari
    Processing Record: 339 of 550 | city:  adre 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=adre
    Processing Record: 340 of 550 | city:  butaritari 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=butaritari
    Processing Record: 341 of 550 | city:  rawannawi 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=rawannawi
    Processing Record: 342 of 550 | city:  meulaboh 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=meulaboh
    Processing Record: 343 of 550 | city:  nikolskoye 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=nikolskoye
    Processing Record: 344 of 550 | city:  korla 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=korla
    Processing Record: 345 of 550 | city:  tezu 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=tezu
    Processing Record: 346 of 550 | city:  berndorf 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=berndorf
    Processing Record: 347 of 550 | city:  jinsha 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=jinsha
    Processing Record: 348 of 550 | city:  lashio 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=lashio
    Processing Record: 349 of 550 | city:  kamaishi 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=kamaishi
    Processing Record: 350 of 550 | city:  shimoda 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=shimoda
    Processing Record: 351 of 550 | city:  susner 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=susner
    Processing Record: 352 of 550 | city:  kletskaya 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=kletskaya
    Processing Record: 353 of 550 | city:  castelldefels 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=castelldefels
    Processing Record: 354 of 550 | city:  shangrao 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=shangrao
    Processing Record: 355 of 550 | city:  sukumo 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=sukumo
    Processing Record: 356 of 550 | city:  boende 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=boende
    Processing Record: 357 of 550 | city:  airai 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=airai
    Processing Record: 358 of 550 | city:  meulaboh 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=meulaboh
    Processing Record: 359 of 550 | city:  butaritari 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=butaritari
    Processing Record: 360 of 550 | city:  tessalit 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=tessalit
    Processing Record: 361 of 550 | city:  rungata 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=rungata
    Processing Record: 362 of 550 | city:  naze 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=naze
    Processing Record: 363 of 550 | city:  butaritari 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=butaritari
    Processing Record: 364 of 550 | city:  airai 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=airai
    Processing Record: 365 of 550 | city:  surt 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=surt
    Processing Record: 366 of 550 | city:  zhezkazgan 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=zhezkazgan
    Processing Record: 367 of 550 | city:  lorengau 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=lorengau
    Processing Record: 368 of 550 | city:  airai 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=airai
    Processing Record: 369 of 550 | city:  det udom 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=det udom
    Processing Record: 370 of 550 | city:  muroto 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=muroto
    Processing Record: 371 of 550 | city:  butaritari 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=butaritari
    Processing Record: 372 of 550 | city:  butaritari 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=butaritari
    Processing Record: 373 of 550 | city:  butaritari 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=butaritari
    Processing Record: 374 of 550 | city:  severo-kurilsk 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=severo-kurilsk
    Processing Record: 375 of 550 | city:  iwaki 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=iwaki
    Processing Record: 376 of 550 | city:  airai 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=airai
    Processing Record: 377 of 550 | city:  buqayq 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=buqayq
    Processing Record: 378 of 550 | city:  glamoc 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=glamoc
    Processing Record: 379 of 550 | city:  nikolskoye 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=nikolskoye
    Processing Record: 380 of 550 | city:  kavieng 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=kavieng
    Processing Record: 381 of 550 | city:  butaritari 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=butaritari
    Processing Record: 382 of 550 | city:  haibowan 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=haibowan
    Processing Record: 383 of 550 | city:  butaritari 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=butaritari
    Processing Record: 384 of 550 | city:  vavuniya 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=vavuniya
    Processing Record: 385 of 550 | city:  akyab 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=akyab
    Processing Record: 386 of 550 | city:  chikoy 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=chikoy
    Processing Record: 387 of 550 | city:  beringovskiy 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=beringovskiy
    Processing Record: 388 of 550 | city:  butaritari 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=butaritari
    Processing Record: 389 of 550 | city:  aflu 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=aflu
    Processing Record: 390 of 550 | city:  butaritari 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=butaritari
    Processing Record: 391 of 550 | city:  odweyne 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=odweyne
    Processing Record: 392 of 550 | city:  butaritari 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=butaritari
    Processing Record: 393 of 550 | city:  darhan 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=darhan
    Processing Record: 394 of 550 | city:  bara 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=bara
    Processing Record: 395 of 550 | city:  nikolskoye 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=nikolskoye
    Processing Record: 396 of 550 | city:  turayf 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=turayf
    Processing Record: 397 of 550 | city:  mahibadhoo 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=mahibadhoo
    Processing Record: 398 of 550 | city:  gonbad-e qabus 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=gonbad-e qabus
    Processing Record: 399 of 550 | city:  vedeno 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=vedeno
    Processing Record: 400 of 550 | city:  beringovskiy 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=beringovskiy
    Processing Record: 401 of 550 | city:  ormara 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=ormara
    Processing Record: 402 of 550 | city:  shingu 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=shingu
    Processing Record: 403 of 550 | city:  viligili 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=viligili
    Processing Record: 404 of 550 | city:  jalingo 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=jalingo
    Processing Record: 405 of 550 | city:  nakamura 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=nakamura
    Processing Record: 406 of 550 | city:  nikolskoye 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=nikolskoye
    Processing Record: 407 of 550 | city:  sibolga 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=sibolga
    Processing Record: 408 of 550 | city:  gonbad-e qabus 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=gonbad-e qabus
    Processing Record: 409 of 550 | city:  chkalovskoye 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=chkalovskoye
    Processing Record: 410 of 550 | city:  lira 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=lira
    Processing Record: 411 of 550 | city:  butaritari 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=butaritari
    Processing Record: 412 of 550 | city:  inderborskiy 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=inderborskiy
    Processing Record: 413 of 550 | city:  butaritari 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=butaritari
    Processing Record: 414 of 550 | city:  salalah 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=salalah
    Processing Record: 415 of 550 | city:  meulaboh 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=meulaboh
    Processing Record: 416 of 550 | city:  severo-kurilsk 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=severo-kurilsk
    Processing Record: 417 of 550 | city:  airai 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=airai
    Processing Record: 418 of 550 | city:  rafai 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=rafai
    Processing Record: 419 of 550 | city:  lasa 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=lasa
    Processing Record: 420 of 550 | city:  ondorhaan 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=ondorhaan
    Processing Record: 421 of 550 | city:  biak 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=biak
    Processing Record: 422 of 550 | city:  yining 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=yining
    Processing Record: 423 of 550 | city:  izumo 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=izumo
    Processing Record: 424 of 550 | city:  mogok 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=mogok
    Processing Record: 425 of 550 | city:  boljarovo 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=boljarovo
    Processing Record: 426 of 550 | city:  butaritari 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=butaritari
    Processing Record: 427 of 550 | city:  dafeng 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=dafeng
    Processing Record: 428 of 550 | city:  jijiga 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=jijiga
    Processing Record: 429 of 550 | city:  hasaki 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=hasaki
    Processing Record: 430 of 550 | city:  butaritari 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=butaritari
    Processing Record: 431 of 550 | city:  kavieng 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=kavieng
    Processing Record: 432 of 550 | city:  sabang 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=sabang
    Processing Record: 433 of 550 | city:  ugoofaaru 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=ugoofaaru
    Processing Record: 434 of 550 | city:  uwayl 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=uwayl
    Processing Record: 435 of 550 | city:  seoul 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=seoul
    Processing Record: 436 of 550 | city:  kollam 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=kollam
    Processing Record: 437 of 550 | city:  azar shahr 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=azar shahr
    Processing Record: 438 of 550 | city:  tahoua 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=tahoua
    Processing Record: 439 of 550 | city:  nikolskoye 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=nikolskoye
    Processing Record: 440 of 550 | city:  hargeysa 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=hargeysa
    Processing Record: 441 of 550 | city:  madinat sittah uktubar 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=madinat sittah uktubar
    Processing Record: 442 of 550 | city:  beringovskiy 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=beringovskiy
    Processing Record: 443 of 550 | city:  ca mau 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=ca mau
    Processing Record: 444 of 550 | city:  kabo 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=kabo
    Processing Record: 445 of 550 | city:  yumen 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=yumen
    Processing Record: 446 of 550 | city:  tangping 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=tangping
    Processing Record: 447 of 550 | city:  sentyabrskiy 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=sentyabrskiy
    Processing Record: 448 of 550 | city:  tonekabon 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=tonekabon
    Processing Record: 449 of 550 | city:  yarada 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=yarada
    Processing Record: 450 of 550 | city:  victoria 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=victoria
    Processing Record: 451 of 550 | city:  lengshuijiang 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=lengshuijiang
    Processing Record: 452 of 550 | city:  butaritari 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=butaritari
    Processing Record: 453 of 550 | city:  kavieng 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=kavieng
    Processing Record: 454 of 550 | city:  bhuban 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=bhuban
    Processing Record: 455 of 550 | city:  kavieng 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=kavieng
    Processing Record: 456 of 550 | city:  hasaki 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=hasaki
    Processing Record: 457 of 550 | city:  staryy krym 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=staryy krym
    Processing Record: 458 of 550 | city:  nikolskoye 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=nikolskoye
    Processing Record: 459 of 550 | city:  tabiauea 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=tabiauea
    Processing Record: 460 of 550 | city:  rungata 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=rungata
    Processing Record: 461 of 550 | city:  butaritari 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=butaritari
    Processing Record: 462 of 550 | city:  hasaki 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=hasaki
    Processing Record: 463 of 550 | city:  sentyabrskiy 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=sentyabrskiy
    Processing Record: 464 of 550 | city:  kuala terengganu 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=kuala terengganu
    Processing Record: 465 of 550 | city:  beringovskiy 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=beringovskiy
    Processing Record: 466 of 550 | city:  manzil salim 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=manzil salim
    Processing Record: 467 of 550 | city:  baherden 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=baherden
    Processing Record: 468 of 550 | city:  victoria 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=victoria
    Processing Record: 469 of 550 | city:  ruswil 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=ruswil
    Processing Record: 470 of 550 | city:  airai 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=airai
    Processing Record: 471 of 550 | city:  kuche 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=kuche
    Processing Record: 472 of 550 | city:  katsuura 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=katsuura
    Processing Record: 473 of 550 | city:  mahibadhoo 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=mahibadhoo
    Processing Record: 474 of 550 | city:  butaritari 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=butaritari
    Processing Record: 475 of 550 | city:  mujiayingzi 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=mujiayingzi
    Processing Record: 476 of 550 | city:  mandalgovi 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=mandalgovi
    Processing Record: 477 of 550 | city:  kloulklubed 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=kloulklubed
    Processing Record: 478 of 550 | city:  boali 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=boali
    Processing Record: 479 of 550 | city:  kavieng 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=kavieng
    Processing Record: 480 of 550 | city:  meulaboh 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=meulaboh
    Processing Record: 481 of 550 | city:  agdam 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=agdam
    Processing Record: 482 of 550 | city:  qui nhon 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=qui nhon
    Processing Record: 483 of 550 | city:  fatehpur 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=fatehpur
    Processing Record: 484 of 550 | city:  kharan 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=kharan
    Processing Record: 485 of 550 | city:  tezu 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=tezu
    Processing Record: 486 of 550 | city:  bargal 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=bargal
    Processing Record: 487 of 550 | city:  itoman 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=itoman
    Processing Record: 488 of 550 | city:  yanan 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=yanan
    Processing Record: 489 of 550 | city:  sindand 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=sindand
    Processing Record: 490 of 550 | city:  matara 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=matara
    Processing Record: 491 of 550 | city:  san mariano 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=san mariano
    Processing Record: 492 of 550 | city:  salalah 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=salalah
    Processing Record: 493 of 550 | city:  kilis 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=kilis
    Processing Record: 494 of 550 | city:  airai 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=airai
    Processing Record: 495 of 550 | city:  chaoyang 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=chaoyang
    Processing Record: 496 of 550 | city:  severo-kurilsk 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=severo-kurilsk
    Processing Record: 497 of 550 | city:  port blair 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=port blair
    Processing Record: 498 of 550 | city:  beringovskiy 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=beringovskiy
    Processing Record: 499 of 550 | city:  airai 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=airai
    Processing Record: 500 of 550 | city:  nikolskoye 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=nikolskoye
    Processing Record: 501 of 550 | city:  lasa 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=lasa
    Processing Record: 502 of 550 | city:  dhidhdhoo 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=dhidhdhoo
    Processing Record: 503 of 550 | city:  huilong 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=huilong
    Processing Record: 504 of 550 | city:  galle 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=galle
    Processing Record: 505 of 550 | city:  banda aceh 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=banda aceh
    Processing Record: 506 of 550 | city:  khandbari 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=khandbari
    Processing Record: 507 of 550 | city:  rungata 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=rungata
    Processing Record: 508 of 550 | city:  lang son 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=lang son
    Processing Record: 509 of 550 | city:  aktash 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=aktash
    Processing Record: 510 of 550 | city:  sinnai 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=sinnai
    Processing Record: 511 of 550 | city:  abha 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=abha
    Processing Record: 512 of 550 | city:  dunayivtsi 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=dunayivtsi
    Processing Record: 513 of 550 | city:  gigmoto 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=gigmoto
    Processing Record: 514 of 550 | city:  pundaguitan 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=pundaguitan
    Processing Record: 515 of 550 | city:  najran 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=najran
    Processing Record: 516 of 550 | city:  vostok 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=vostok
    Processing Record: 517 of 550 | city:  beringovskiy 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=beringovskiy
    Processing Record: 518 of 550 | city:  hambantota 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=hambantota
    Processing Record: 519 of 550 | city:  aitape 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=aitape
    Processing Record: 520 of 550 | city:  severo-kurilsk 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=severo-kurilsk
    Processing Record: 521 of 550 | city:  davila 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=davila
    Processing Record: 522 of 550 | city:  mukhen 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=mukhen
    Processing Record: 523 of 550 | city:  lorengau 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=lorengau
    Processing Record: 524 of 550 | city:  beringovskiy 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=beringovskiy
    Processing Record: 525 of 550 | city:  paralimni 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=paralimni
    Processing Record: 526 of 550 | city:  nikolskoye 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=nikolskoye
    Processing Record: 527 of 550 | city:  mahon 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=mahon
    Processing Record: 528 of 550 | city:  ondorhaan 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=ondorhaan
    Processing Record: 529 of 550 | city:  waddan 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=waddan
    Processing Record: 530 of 550 | city:  hasaki 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=hasaki
    Processing Record: 531 of 550 | city:  gaozhou 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=gaozhou
    Processing Record: 532 of 550 | city:  sentyabrskiy 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=sentyabrskiy
    Processing Record: 533 of 550 | city:  xining 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=xining
    Processing Record: 534 of 550 | city:  kazanka 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=kazanka
    Processing Record: 535 of 550 | city:  bac can 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=bac can
    Processing Record: 536 of 550 | city:  mae hong son 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=mae hong son
    Processing Record: 537 of 550 | city:  abha 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=abha
    Processing Record: 538 of 550 | city:  zhezkazgan 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=zhezkazgan
    Processing Record: 539 of 550 | city:  petropavlovka 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=petropavlovka
    Processing Record: 540 of 550 | city:  shimoda 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=shimoda
    Processing Record: 541 of 550 | city:  syracuse 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=syracuse
    Processing Record: 542 of 550 | city:  kazalinsk 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=kazalinsk
    Processing Record: 543 of 550 | city:  surt 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=surt
    Processing Record: 544 of 550 | city:  katsuura 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=katsuura
    Processing Record: 545 of 550 | city:  butaritari 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=butaritari
    Processing Record: 546 of 550 | city:  garh maharaja 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=garh maharaja
    Processing Record: 547 of 550 | city:  meulaboh 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=meulaboh
    Processing Record: 548 of 550 | city:  rungata 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=rungata
    Processing Record: 549 of 550 | city:  lorengau 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=lorengau
    Processing Record: 550 of 550 | city:  rungata 
     http://api.openweathermap.org/data/2.5/weather?appid=7be7dfb02672af49d73e9ca689405225&units=metric&q=rungata



```python
#weather_response_json
```


```python
# Extract interesting data from big list
city_data = [data.get("name") for data in weather_data_list]
cloud_data = [data.get("clouds",{}).get("all",{}) for data in weather_data_list]
country_data = [data.get("sys",{}).get("country",{}) for data in weather_data_list]
date_data = [data.get("dt") for data in weather_data_list]
humidity_data = [data.get("main",{}).get("humidity",{}) for data in weather_data_list]
lat_data = [data.get("coord",{}).get("lat",{}) for data in weather_data_list]
lon_data = [data.get("coord",{}).get("lat",{}) for data in weather_data_list]
max_temp_data = [data.get("main",{}).get("temp_max",{}) for data in weather_data_list]
wind_speed_data = [data.get("wind",{}).get("speed",{}) for data in weather_data_list]
```


```python
#creating weather_data_dict to create DataFrame
weather_data_dict = {"Date": date_data,
                     "City": city_data,
                     "Country":country_data,
                     "Lon": lon_data,
                     "Lat": lat_data,
                     "Max Temp": max_temp_data,
                     "Humidity": humidity_data,
                     "Cloudiness":cloud_data,
                     "Wind Speed":wind_speed_data}
```


```python
#Creating DataFrame
weather_data_df = pd.DataFrame(weather_data_dict)
#weather_data_df.count()
weather_data_df = weather_data_df.dropna(how='any')
#weather_data_df.count()
weather_data_df['Max Temp'] = weather_data_df['Max Temp'] * 1.8 + 32
weather_data_df.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>City</th>
      <th>Cloudiness</th>
      <th>Country</th>
      <th>Date</th>
      <th>Humidity</th>
      <th>Lat</th>
      <th>Lon</th>
      <th>Max Temp</th>
      <th>Wind Speed</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Aden</td>
      <td>12</td>
      <td>YE</td>
      <td>1.509331e+09</td>
      <td>100</td>
      <td>12.78</td>
      <td>12.78</td>
      <td>81.95</td>
      <td>8.61</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Beringovskiy</td>
      <td>0</td>
      <td>RU</td>
      <td>1.509331e+09</td>
      <td>100</td>
      <td>63.05</td>
      <td>63.05</td>
      <td>20.516</td>
      <td>1.31</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Kulhudhuffushi</td>
      <td>88</td>
      <td>MV</td>
      <td>1.509331e+09</td>
      <td>100</td>
      <td>6.62</td>
      <td>6.62</td>
      <td>80.024</td>
      <td>4.91</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Severo-Kurilsk</td>
      <td>92</td>
      <td>RU</td>
      <td>1.509331e+09</td>
      <td>98</td>
      <td>50.68</td>
      <td>50.68</td>
      <td>41.594</td>
      <td>10.61</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Zaysan</td>
      <td>32</td>
      <td>KZ</td>
      <td>1.509331e+09</td>
      <td>81</td>
      <td>47.47</td>
      <td>47.47</td>
      <td>38.084</td>
      <td>0.96</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Build a scatter plot for each data type
plt.scatter(weather_data_df["Lat"], weather_data_df["Max Temp"], marker="o")

# Incorporate the other graph properties
plt.title("Temperature in World Cities")
plt.ylabel("Temperature (FAHRENHEIT)")
plt.xlabel("Latitude")
plt.grid(True)

# Save the figure
plt.savefig("TemperatureInWorldCities_Temperature.png")

# Show plot
plt.show()
```


![png](output_8_0.png)



```python
# Build a scatter plot for each data type
plt.scatter(weather_data_df["Lat"], weather_data_df["Humidity"], marker="o")

# Incorporate the other graph properties
plt.title("Humidity in World Cities")
plt.ylabel("Humidity")
plt.xlabel("Latitude")
plt.grid(True)

# Save the figure
plt.savefig("TemperatureInWorldCities_Humidity.png")

# Show plot
plt.show()
```


![png](output_9_0.png)



```python
# Build a scatter plot for each data type
plt.scatter(weather_data_df["Lat"], weather_data_df["Cloudiness"], marker="o")

# Incorporate the other graph properties
plt.title("Cloudiness in World Cities")
plt.ylabel("Cloudiness")
plt.xlabel("Latitude")
plt.grid(True)

# Save the figure
plt.savefig("TemperatureInWorldCities_Cloudiness.png")

# Show plot
plt.show()
```


![png](output_10_0.png)



```python
# Build a scatter plot for each data type
plt.scatter(weather_data_df["Lat"], weather_data_df["Wind Speed"], marker="o")

# Incorporate the other graph properties
plt.title("Temperature in World Cities")
plt.ylabel("Wind Speed")
plt.xlabel("Latitude")
plt.grid(True)

# Save the figure
plt.savefig("TemperatureInWorldCities_WindSpeed.png")

# Show plot
plt.show()
```


![png](output_11_0.png)

