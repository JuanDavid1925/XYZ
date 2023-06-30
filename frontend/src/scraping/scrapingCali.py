from bs4 import BeautifulSoup
import requests
import pandas as pd

urlCali = 'https://www.booking.com/searchresults.es.html?aid=356980&label=gog235jc-1DCAMYyAEoMkIEY2FsaUgKWANoMogBAZgBCrgBF8gBD9gBA-gBAfgBAogCAagCA7gC3ar6pAbAAgHSAiQwMjllYTlmYS1iOGI0LTRlZmItYjViMC1kYjM0ZDdiOGI0OWHYAgTgAgE&sid=fdd0d7f0916be7f3ad8a51a712a0efbb&sb=1&sb_lp=1&src=theme_landing_city&src_elem=sb&error_url=https%3A%2F%2Fwww.booking.com%2Ffivestars%2Fcity%2Fco%2Fcali.es.html%3Faid%3D356980%26label%3Dgog235jc-1DCAMYyAEoMkIEY2FsaUgKWANoMogBAZgBCrgBF8gBD9gBA-gBAfgBAogCAagCA7gC3ar6pAbAAgHSAiQwMjllYTlmYS1iOGI0LTRlZmItYjViMC1kYjM0ZDdiOGI0OWHYAgTgAgE%26sid%3Dfdd0d7f0916be7f3ad8a51a712a0efbb%26&top_ufis=0&theme_id=58&theme_source=theme_landing_city&ss=Cali&is_ski_area=0&ssne=Cali&ssne_untouched=Cali&dest_id=-579248&dest_type=city&checkin_year=2023&checkin_month=7&checkin_monthday=8&checkout_year=2023&checkout_month=7&checkout_monthday=9&efdco=1&group_adults=2&group_children=0&no_rooms=1&b_h4u_keep_filters=&from_sf=1'
page = requests.get(urlCali, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0'})
soup = BeautifulSoup(page.content, 'html.parser')

#Hoteles

nombreHoteles = list()
precios = list()
habitaciones = list()
fotoHotel = list()

nombreHotelCali = soup.find_all('div', class_='fcab3ed991 a23c043802')
precioHotelCali = soup.find_all('span', class_ = 'fcab3ed991 fbd1d3018c e729ed5ab6')
habitacionHotelCali = soup.find_all('span', class_ = 'df597226dd')
fotoHotelCali = soup.find_all('img', class_ = 'b8b0793b0e')

count = 0
for i in nombreHotelCali:
    if count < 5:
        nombreHoteles.append(i.text)
    else:
        break
    count += 1

count = 0
for j in precioHotelCali:
    if count < 5:
        precios.append(j.text[4:14])
    else:
        break
    count += 1

count = 0
for i in habitacionHotelCali:
    if count < 5:
        habitaciones.append(i.text)
    else:
        break
    count += 1
    
count = 0
for i in fotoHotelCali:
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