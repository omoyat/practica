#pip install beautifulsoup4

from bs4 import BeautifulSoup
import requests
url = 'https://www.bolsamadrid.es/esp/aspx/Mercados/Precios.aspx?indice=ESI100000000&punto=indice'
req = requests.get(url)
soup = BeautifulSoup(req.content, "html.parser")


# Extraer todas los nombre del archivo HTML

 
empresas = soup.find_all(attrs={'class':'DifFlBj'})
for empresa in empresas:

    empresastxt = empresa.get_text()

    for col in empresa.next_siblings:

        if col.name:

            print(col.get_text())