#Al:Par ou impar com a máquina. Jogador perder o loop para, contando vitórias consecutivas.
#autor: Lucas Borguezam
#data:

#Import
from random import randint
#Inicio
t = i = 0
print("=-"*20)
print("Vamos Jogar PAr ou Ímpar")
print("=-"*20)
while True:
    vj = int(input("Diga um valor: "))
    maquina = randint(0,10)
    t = vj+maquina
    while PouI not in 'pi':
        PouI = str(input("Par ou Ímpar? [P/I]: ").lower().strip()[0])
    if (PouI == "i"):
        if( (t%2) != 0):
            i+=1
            print(f"{t} é Impar Você venceu!!")
            print("Jogue Novamente...")
        else:
            print((f"{t} é Par, Você Perdeu"))
            break
    elif (PouI == "p"):
        if ((t % 2) == 0):
            i += 1
            print(f"{t} é Par Você venceu!!")
        else:
            print((f"{t} é Impar, Você Perdeu"))
            break
print(f"Fim de Jogo.\n\nVocê venceu {i}x consecutivas.".upper())
#fim
