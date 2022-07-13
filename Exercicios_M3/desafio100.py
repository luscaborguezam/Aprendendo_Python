#Al:
#autor: Lucas Borguezam
#data:

#Import
from random import randint
from time import sleep
#Inicio


def Sorteia(lst):
    print("Sorteando 5 valores da lista: ", end='')
    for n in range(0, 6):
        lst.append(randint(0, 10))
        print(lst[n], end=' ')
        sleep(0.3)
    print("Pronto!")


def SomaPar(lst):
    print(f"Somando os valores pares de {lst} temos ", end='')
    sp = 0
    for n in lst:
        if n%2 == 0:
            sp += n
    print(sp)


numeros = list()
Sorteia(numeros)
SomaPar(numeros)
#fim
