from bs4 import BeautifulSoup
import requests

def scraping(ciudad):
    url = ''
    if ciudad == "Bogota":
        url = 'https://www.booking.com/searchresults.es.html?label=gog235jc-1DCAMYyAEoMkIEY2FsaUgKWANoMogBAZgBCrgBF8gBD9gBA-gBAfgBAogCAagCA7gC3ar6pAbAAgHSAiQwMjllYTlmYS1iOGI0LTRlZmItYjViMC1kYjM0ZDdiOGI0OWHYAgTgAgE&sid=fdd0d7f0916be7f3ad8a51a712a0efbb&aid=356980&ss=Bogot%C3%A1%2C+Colombia&ssne=Cali&ssne_untouched=Cali&lang=es&src=searchresults&dest_id=-578472&dest_type=city&ac_position=0&ac_click_type=b&ac_langcode=es&ac_suggestion_list_length=5&search_selected=true&search_pageview_id=89573d42f455022e&ac_meta=GhA4OTU3M2Q0MmY0NTUwMjJlIAAoATICZXM6AkJvQABKAFAA&checkin=2023-07-08&checkout=2023-07-09&group_adults=2&no_rooms=1&group_children=0&nflt=class%3D5'
    elif ciudad == "Cali":
        url = 'https://www.booking.com/searchresults.es.html?aid=356980&label=gog235jc-1DCAMYyAEoMkIEY2FsaUgKWANoMogBAZgBCrgBF8gBD9gBA-gBAfgBAogCAagCA7gC3ar6pAbAAgHSAiQwMjllYTlmYS1iOGI0LTRlZmItYjViMC1kYjM0ZDdiOGI0OWHYAgTgAgE&sid=fdd0d7f0916be7f3ad8a51a712a0efbb&sb=1&sb_lp=1&src=theme_landing_city&src_elem=sb&error_url=https%3A%2F%2Fwww.booking.com%2Ffivestars%2Fcity%2Fco%2Fcali.es.html%3Faid%3D356980%26label%3Dgog235jc-1DCAMYyAEoMkIEY2FsaUgKWANoMogBAZgBCrgBF8gBD9gBA-gBAfgBAogCAagCA7gC3ar6pAbAAgHSAiQwMjllYTlmYS1iOGI0LTRlZmItYjViMC1kYjM0ZDdiOGI0OWHYAgTgAgE%26sid%3Dfdd0d7f0916be7f3ad8a51a712a0efbb%26&top_ufis=0&theme_id=58&theme_source=theme_landing_city&ss=Cali&is_ski_area=0&ssne=Cali&ssne_untouched=Cali&dest_id=-579248&dest_type=city&checkin_year=2023&checkin_month=7&checkin_monthday=8&checkout_year=2023&checkout_month=7&checkout_monthday=9&efdco=1&group_adults=2&group_children=0&no_rooms=1&b_h4u_keep_filters=&from_sf=1'
    elif ciudad == "Cartagena":
        url = 'https://www.booking.com/searchresults.es.html?label=gog235jc-1DCAMYyAEoMkIEY2FsaUgKWANoMogBAZgBCrgBF8gBD9gBA-gBAfgBAogCAagCA7gC3ar6pAbAAgHSAiQwMjllYTlmYS1iOGI0LTRlZmItYjViMC1kYjM0ZDdiOGI0OWHYAgTgAgE&sid=fdd0d7f0916be7f3ad8a51a712a0efbb&aid=356980&ss=Cartagena+de+Indias%2C+Colombia&ssne=Medell%C3%ADn&ssne_untouched=Medell%C3%ADn&lang=es&src=searchresults&dest_id=-579943&dest_type=city&checkin=2023-07-08&checkout=2023-07-09&group_adults=2&no_rooms=1&group_children=0&nflt=class%3D5'
    elif ciudad == "Dubai":
        url = 'https://www.booking.com/searchresults.es.html?label=gog235jc-1DCAMYyAEoMkIEY2FsaUgKWANoMogBAZgBCrgBF8gBD9gBA-gBAfgBAogCAagCA7gC3ar6pAbAAgHSAiQwMjllYTlmYS1iOGI0LTRlZmItYjViMC1kYjM0ZDdiOGI0OWHYAgTgAgE&sid=fdd0d7f0916be7f3ad8a51a712a0efbb&aid=356980&ss=Dub%C3%A1i%2C+Dub%C3%A1i%2C+Emiratos+%C3%81rabes+Unidos&ssne=Londres&ssne_untouched=Londres&lang=es&src=searchresults&dest_id=-782831&dest_type=city&ac_position=0&ac_click_type=b&ac_langcode=es&ac_suggestion_list_length=5&search_selected=true&search_pageview_id=e3f046c7118402a7&ac_meta=GhBlM2YwNDZjNzExODQwMmE3IAAoATICZXM6BGR1YmFAAEoAUAA%3D&checkin=2023-07-08&checkout=2023-07-09&group_adults=2&no_rooms=1&group_children=0&nflt=class%3D5'
    elif ciudad == "Londres":
        url = 'https://www.booking.com/searchresults.es.html?label=gog235jc-1DCAMYyAEoMkIEY2FsaUgKWANoMogBAZgBCrgBF8gBD9gBA-gBAfgBAogCAagCA7gC3ar6pAbAAgHSAiQwMjllYTlmYS1iOGI0LTRlZmItYjViMC1kYjM0ZDdiOGI0OWHYAgTgAgE&sid=fdd0d7f0916be7f3ad8a51a712a0efbb&aid=356980&ss=Londres%2C+Gran+Londres%2C+Reino+Unido&ssne=Madrid&ssne_untouched=Madrid&lang=es&src=searchresults&dest_id=-2601889&dest_type=city&ac_position=0&ac_click_type=b&ac_langcode=es&ac_suggestion_list_length=5&search_selected=true&search_pageview_id=b34346985445014b&ac_meta=GhBiMzQzNDY5ODU0NDUwMTRiIAAoATICZXM6BmxvbmRyZUAASgBQAA%3D%3D&checkin=2023-07-08&checkout=2023-07-09&group_adults=2&no_rooms=1&group_children=0&nflt=class%3D5'
    elif ciudad == "Madrid":
        url = 'https://www.booking.com/searchresults.es.html?label=gog235jc-1DCAMYyAEoMkIEY2FsaUgKWANoMogBAZgBCrgBF8gBD9gBA-gBAfgBAogCAagCA7gC3ar6pAbAAgHSAiQwMjllYTlmYS1iOGI0LTRlZmItYjViMC1kYjM0ZDdiOGI0OWHYAgTgAgE&sid=fdd0d7f0916be7f3ad8a51a712a0efbb&aid=356980&ss=Madrid%2C+Comunidad+de+Madrid%2C+Espa%C3%B1a&ssne=Par%C3%ADs&ssne_untouched=Par%C3%ADs&lang=es&src=searchresults&dest_id=-390625&dest_type=city&ac_position=0&ac_click_type=b&ac_langcode=es&ac_suggestion_list_length=5&search_selected=true&search_pageview_id=8aa1467ac2f6000f&ac_meta=GhA4YWExNDY3YWMyZjYwMDBmIAAoATICZXM6BG1hZHJAAEoAUAA%3D&checkin=2023-07-08&checkout=2023-07-09&group_adults=2&no_rooms=1&group_children=0&nflt=class%3D5'
    elif ciudad == "Medellin":
        url = 'https://www.booking.com/searchresults.es.html?label=gog235jc-1DCAMYyAEoMkIEY2FsaUgKWANoMogBAZgBCrgBF8gBD9gBA-gBAfgBAogCAagCA7gC3ar6pAbAAgHSAiQwMjllYTlmYS1iOGI0LTRlZmItYjViMC1kYjM0ZDdiOGI0OWHYAgTgAgE&sid=fdd0d7f0916be7f3ad8a51a712a0efbb&aid=356980&ss=Medell%C3%ADn%2C+Antioquia%2C+Colombia&ssne=Bogot%C3%A1&ssne_untouched=Bogot%C3%A1&lang=es&src=searchresults&dest_id=-592318&dest_type=city&ac_position=0&ac_click_type=b&ac_langcode=es&ac_suggestion_list_length=5&search_selected=true&search_pageview_id=ad5a435d2eeb00fd&ac_meta=GhBhZDVhNDM1ZDJlZWIwMGZkIAAoATICZXM6A01lZEAASgBQAA%3D%3D&checkin=2023-07-08&checkout=2023-07-09&group_adults=2&no_rooms=1&group_children=0&nflt=class%3D5'
    elif ciudad == "Paris":
        url = 'https://www.booking.com/searchresults.es.html?label=gog235jc-1DCAMYyAEoMkIEY2FsaUgKWANoMogBAZgBCrgBF8gBD9gBA-gBAfgBAogCAagCA7gC3ar6pAbAAgHSAiQwMjllYTlmYS1iOGI0LTRlZmItYjViMC1kYjM0ZDdiOGI0OWHYAgTgAgE&sid=fdd0d7f0916be7f3ad8a51a712a0efbb&aid=356980&ss=Par%C3%ADs%2C+%C3%8Ele-de-France%2C+Francia&ssne=Venecia&ssne_untouched=Venecia&lang=es&src=searchresults&dest_id=-1456928&dest_type=city&ac_position=0&ac_click_type=b&ac_langcode=es&ac_suggestion_list_length=5&search_selected=true&search_pageview_id=76104641f5b601bf&ac_meta=GhA3NjEwNDY0MWY1YjYwMWJmIAAoATICZXM6BHBhcmlAAEoAUAA%3D&checkin=2023-07-08&checkout=2023-07-09&group_adults=2&no_rooms=1&group_children=0&nflt=class%3D5'
    elif ciudad == "San Andres":
        url = 'https://www.booking.com/searchresults.es.html?label=gog235jc-1DCAMYyAEoMkIEY2FsaUgKWANoMogBAZgBCrgBF8gBD9gBA-gBAfgBAogCAagCA7gC3ar6pAbAAgHSAiQwMjllYTlmYS1iOGI0LTRlZmItYjViMC1kYjM0ZDdiOGI0OWHYAgTgAgE&sid=fdd0d7f0916be7f3ad8a51a712a0efbb&aid=356980&ss=San+Andr%C3%A9s%2C+Islas+San+Andr%C3%A9s+y+Providencia%2C+Colombia&ssne=Cartagena+de+Indias&ssne_untouched=Cartagena+de+Indias&lang=es&src=searchresults&dest_id=-597118&dest_type=city&ac_position=0&ac_click_type=b&ac_langcode=es&ac_suggestion_list_length=5&search_selected=true&search_pageview_id=347545837cc201a4&ac_meta=GhAzNDc1NDU4MzdjYzIwMWE0IAAoATICZXM6A3NhbkAASgBQAA%3D%3D&checkin=2023-07-08&checkout=2023-07-09&group_adults=2&no_rooms=1&group_children=0&nflt=mealplan%3D1'
    elif ciudad == "Venecia":
        url = 'https://www.booking.com/searchresults.es.html?label=gog235jc-1DCAMYyAEoMkIEY2FsaUgKWANoMogBAZgBCrgBF8gBD9gBA-gBAfgBAogCAagCA7gC3ar6pAbAAgHSAiQwMjllYTlmYS1iOGI0LTRlZmItYjViMC1kYjM0ZDdiOGI0OWHYAgTgAgE&sid=fdd0d7f0916be7f3ad8a51a712a0efbb&aid=356980&ss=Venecia%2C+V%C3%A9neto%2C+Italia&ssne=Cali&ssne_untouched=Cali&lang=es&src=searchresults&dest_id=-132007&dest_type=city&ac_position=0&ac_click_type=b&ac_langcode=es&ac_suggestion_list_length=5&search_selected=true&search_pageview_id=6be6462911e10280&ac_meta=GhA2YmU2NDYyOTExZTEwMjgwIAAoATICZXM6BXZlbmVjQABKAFAA&checkin=2023-07-08&checkout=2023-07-09&group_adults=2&no_rooms=1&group_children=0&nflt=class%3D5'
    else:
        print("lloro")
    page = requests.get(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0'})
    soup = BeautifulSoup(page.content, 'html.parser')

    #Hoteles

    nombreHoteles = list()
    precios = list()
    habitaciones = list()
    fotoHoteles = list()

    nombreHotel = soup.find_all('div', class_='fcab3ed991 a23c043802')
    precioHotel = soup.find_all('span', class_ = 'fcab3ed991 fbd1d3018c e729ed5ab6')
    habitacionHotel = soup.find_all('span', class_ = 'df597226dd')
    fotoHotel = soup.find_all('img', class_ = 'b8b0793b0e')

    count = 0
    for i in nombreHotel:
        if count < 5:
            nombreHoteles.append(i.text)
        else:
            break
        count += 1

    count = 0
    for j in precioHotel:
        if count < 5:
            precios.append(j.text[4:14])
        else:
            break
        count += 1

    count = 0
    for i in habitacionHotel:
        if count < 5:
            habitaciones.append(i.text)
        else:
            break
        count += 1
        
    count = 0
    for i in fotoHotel:
        if count < 5:
            fotoHoteles.append(i.get('src'))
        else:
            break
        count += 1
    
    resultado = [nombreHoteles,precios,habitaciones,fotoHoteles]
    return resultado