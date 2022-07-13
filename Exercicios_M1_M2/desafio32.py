#Al: Programa que recebe o ano e diga se é bisexto
#autor: Lucas Borguezam
#data:07/04

#Import
from datetime import date
#Inicio
ano = int(input("Que ano quer analisar? "))
#Ano bissexto é a cada 4 anos, exceto anos multiplos de 100 que não são multiplos de 400
if ano == 0:
    ano = date.today().year#Cod. pga o ano atual da máquina e coloca na variável

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 ==0:
    print("O ano {} é BISSEXTO".format(ano))
else:
    print("O ano {} não é BISSEXTO".format(ano))
#fim
