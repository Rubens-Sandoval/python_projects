from bs4 import BeautifulSoup

import requests

#Recebe todo o conteúdo da requisição http do site.
site = requests.get("https://www.climatempo.com.br").content

# armazena o html da página.
soup = BeautifulSoup(site, 'html.parser')

# transforma o html em string e exibe.
#print(soup.prettify())

temperatura = soup.find("p", class_="-gray _flex _align-center")

print(temperatura)