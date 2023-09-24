import requests
import mysql.connector
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
        movie = cells[2].text.strip()
        box_office = cells[4].text.strip()

        data.append({'Movie': movie, 'Box Office': box_office})

    host = 'localhost'
    user = 'root'
    password = '1234'
    database = 'movies'

    try:
        conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )

        cursor = conn.cursor()

        for item in data:
            movie = item['Movie']
            box_office = item['Box Office']

            insert_query = "INSERT INTO filmes (titulo, bilheteria) VALUES (%s, %s)"

            cursor.execute(insert_query, (movie, box_office))

        conn.commit()

    except mysql.connector.Error as error:
        print(f"Error: {error}")

    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

else:
    print('Results not found')
