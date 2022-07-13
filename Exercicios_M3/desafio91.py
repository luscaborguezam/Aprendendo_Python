#Al: 4 jogadores, jogam dado, guardar o resultado em um dict(), no final mostrar em ordem o resultado,
# Ganha quem tirar o número maior
#autor: Lucas Borguezam
#data:

#Import
from random import randint
from time import sleep
from operator import itemgetter #usado para pegar itens especificos de um dicionário como em uma lista
#Inicio
print("Resultado das Jogadas: ")
jogada = {  'Jogador1' : randint(1, 6),
            'Jogador2' : randint(1, 6),
            'Jogador3' : randint(1, 6),
            'Jogador4' : randint(1, 6)  }
for k, v in jogada.items():
    print(f"O {k} tirou {v}.")
    sleep(0.5)
ranking = dict
# itemgetter transforma ranking(dicionário) em uma lista
# itemgetter(1) define qual item do dicionário estará em comparação
print(jogada)
ranking = sorted(jogada.items(), key=itemgetter(1), reverse=True)
print(ranking)
# sorted = ordena uma lista, reverse coloca ela na ordem reversa.
print(f"{'Ranking  dos jogadores':=^30}")
for i, v in enumerate(ranking):
    print(f'{i+1}° Lugar: {v[0]} com {v[1]}')
    sleep(0.5)

#fim
