from bs4 import BeautifulSoup
import requests
import pandas as pd

urlVenecia = 'https://www.booking.com/searchresults.es.html?label=gog235jc-1DCAMYyAEoMkIEY2FsaUgKWANoMogBAZgBCrgBF8gBD9gBA-gBAfgBAogCAagCA7gC3ar6pAbAAgHSAiQwMjllYTlmYS1iOGI0LTRlZmItYjViMC1kYjM0ZDdiOGI0OWHYAgTgAgE&sid=fdd0d7f0916be7f3ad8a51a712a0efbb&aid=356980&ss=Venecia%2C+V%C3%A9neto%2C+Italia&ssne=Cali&ssne_untouched=Cali&lang=es&src=searchresults&dest_id=-132007&dest_type=city&ac_position=0&ac_click_type=b&ac_langcode=es&ac_suggestion_list_length=5&search_selected=true&search_pageview_id=6be6462911e10280&ac_meta=GhA2YmU2NDYyOTExZTEwMjgwIAAoATICZXM6BXZlbmVjQABKAFAA&checkin=2023-07-08&checkout=2023-07-09&group_adults=2&no_rooms=1&group_children=0&nflt=class%3D5'
page = requests.get(urlVenecia, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0'})
soup = BeautifulSoup(page.content, 'html.parser')

#Hoteles

nombreHoteles = list()
precios = list()
habitaciones = list()
fotoHotel = list()

nombreHotelVenecia = soup.find_all('div', class_='fcab3ed991 a23c043802')
precioHotelVenecia = soup.find_all('span', class_ = 'fcab3ed991 fbd1d3018c e729ed5ab6')
habitacionHotelVenecia = soup.find_all('span', class_ = 'df597226dd')
fotoHotelVenecia = soup.find_all('img', class_ = 'b8b0793b0e')

count = 0
for i in nombreHotelVenecia:
    if count < 5:
        nombreHoteles.append(i.text)
    else:
        break
    count += 1

count = 0
for j in precioHotelVenecia:
    if count < 5:
        precios.append(j.text[4:14])
    else:
        break
    count += 1

count = 0
for i in habitacionHotelVenecia:
    if count < 5:
        habitaciones.append(i.text)
    else:
        break
    count += 1
    
count = 0
for i in fotoHotelVenecia:
    if count < 5:
        fotoHotel.append(i.get('src'))
    else:
        break
    count += 1

tabla = pd.DataFrame({'Nombre':nombreHoteles, 'Precios':precios, 'Habitaciones': habitaciones, 'Foto':fotoHotel}, index=list(range(1,6)))

print(nombreHoteles)
print(precios)
print(habitaciones)
print(fotoHotel)
print(tabla)