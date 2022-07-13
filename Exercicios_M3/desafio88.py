#Al: Programa que palpite o tanto que o usuário quiser, e desenvolva cada palpite,
# com números aleatórios, e a sequencia não pode se repetir
#autor: Lucas Borguezam
#data:

#Import
from random import randint
from time import sleep
#Inicio
palpites = list()
palpite = list()
np = int(input("Quantos jogos você quer q eu sorteie?"))

for c in range(0, np):
    for i in range(0, 6):
        palpite.append(randint(0, 100))
    if palpite not in palpites:
        palpite.sort()
        palpites.append(palpite[:])
    else:
        c -= 1
    palpite.clear()

print(f"{'Sorteando os jogos:':=^30}")
for n, c in enumerate(palpites):
    print(f"Jogo {n+1}: {c}")
    sleep(0.3)
print(f"{'Boa sorte':=^30}")
#fim
