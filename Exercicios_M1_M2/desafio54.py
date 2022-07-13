#Al: leia ano de nascimento de 7 pessoas, mostrar quantos nã oatingiram a maior idade
#autor: Lucas Borguezam
#data:

#Import
from datetime import date
#Inicio
menor = 0
maior = 0
anoAtual = date.today().year

for pessoas in range(1, 8):
    anoNascimento = int(input("em que ano a {}° pessoa nasceu?".format(pessoas)))
    idade = anoAtual - anoNascimento
    if idade >= 21:
        maior += 1
    else:
        menor += 1
print("maior idadede: {}.\nmenor idade: {}.".format(maior, menor))
#fim
