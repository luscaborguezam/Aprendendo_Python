#Al: 5 números aleatórios q serão armazenados em uma tupla, mostrando eles e o menor e maior valor inserido
#autor: Lucas Borguezam
#data:

#Import
from random import randint
#Inicio

aleatorios = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
for n in aleatorios:
    print(f"{n}, ", end='')
print(f"\nO maior valor sorteado foi {max(aleatorios)}")
print(f"O menor valor sorteado foi {min(aleatorios)}")

#fim
