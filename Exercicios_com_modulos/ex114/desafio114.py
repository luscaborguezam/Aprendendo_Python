#Al:Programa que informa se o site pudim.com.br está acessivel.
#autor: Lucas Borguezam
#data:

#Import
import urllib
import urllib.request
#inicio
try:
    site = 'http://pudim.com.br'
    conection = urllib.request.urlopen(site)
except urllib.error.URLError:
    print("\033[0;31mO Site está inacessível no momento.")
else:
    print(f"Conseguiu acessar o site {site} com sucesso!")
    print(conection.read()) #pega do sites seu conteudo html
#fim