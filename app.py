import requests
from bs4 import BeautifulSoup

url = 'https://pt.wikipedia.org/wiki/Lista_de_filmes_de_maior_bilheteria'
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    table = soup.find('table')
    data = []
    rows = table.find_all('tr')[1:]

    for row in rows:
        cells = row.find_all('td')
        movie = cells[2].text
        box_office = cells[4].text

        data.append({'Movie': movie, 'Box Office': box_office})

    for item in data:
        print(f"Movie: {item['Movie']}, Box Office: {item['Box Office']}")

else:
    print('Results not found')
