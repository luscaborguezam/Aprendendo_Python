#Al: Jogo da adivinhação exercicio 28, com while
#autor: Lucas Borguezam
#data:

#Import
from random import randint
#Inicio;
# Resolução
# CPU = 0
# jogador = -1
# while CPU != jogador:
#     CPU = randint(0, 10)
#     jogador = int(input("Adivinhe qual número estou pensando de 0 a 10?\n")).strip()
#     print("\nCPU: {}\nJogador: {}".format(CPU, jogador))
#     if(CPU == jogador):
#         print("Parabens você acertou")
#     else:
#         print("Errado tente novamente")
# print("Fim")

# correção
CPU = randint(0, 10)
print('Sou seu computador... Acabei de pensar em um número entre 0 e 10.')
print('Acerte qual foi!')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é seu palpite?'))
    palpites += 1
    if jogador == CPU:
        acertou = True
    else:
        print("\033[1;31mTente novamente!\033[m")
        if jogador > CPU:
            print("Dica: Número é menor")
        else:
            print("Dica: Número é maior")

print("Acertou com {} tentativas Paraboins!".format(palpites))
#fim
