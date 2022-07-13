#Al: programa q faz o computador jogar jokenpo
#autor: Lucas Borguezam
#data:

#Import
import random
from time import sleep
#Inicio
#Criando opções
jokenpo = {0:'PEDRA', 1:'PAPEL' , 2:'TESOURA'}
print("Suas opções:\n"
      "[0] PEDRA\n"
      "[1] PAPEL\n"
      "[2]TESOURA")
#Recebendo opções
user = int(input(print("Escolha: ")))
maquina = random.randint(0, 2)
print("Jo")
sleep(0.5)
print("KEN")
sleep(0.5)
print("PO!!")
# Mostrando opções escolhidas
print("Player:{}".format(jokenpo[user]))
print("Máquina:{}".format(jokenpo[maquina]))
# verficação do vencedor
if (maquina == 0 and user == 2) or (maquina == 1 and user == 0) or (maquina == 2 and user == 1):
     print("- MAQUINA: Ganheeiii")
elif maquina == user:
    print("- MÁQUINA: EMPATE!!")
else:
    print("- MÁQUINA: A próxima vencerei")
#fim
