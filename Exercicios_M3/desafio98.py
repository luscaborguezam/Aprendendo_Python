#Al: Função contador() recebendo 3 parêmetros, iniciom fim, e passo.
# a) de 1 até 10, em 1 em 1
# b) de 10 até 0, de 2 em 2
# c) contagem personalizada
#autor: Lucas Borguezam
#data:

#Import
from time import sleep
#Inicio


def Contador(inicio, fim, passo):
    if passo == 0:
        passo = 1
    if passo < 0:
        passo *= -1
    print("-="*40)
    if inicio <= fim:
        print(f"Contagem de {inicio} até {fim} em {passo} e {passo}")
        for num in range(inicio, fim+1, passo):
            print(num, end=' ')
            sleep(0.2)
    else:
        print(f"Contagem de {inicio} até {fim} em {passo} e {passo}")
        for num in range(inicio, fim-1, -passo):
            print(num, end=' ')
            sleep(0.2)
    print("FIM!")


Contador(1, 10, 1)
Contador(10, 0, 2)
print("Personalíze a contagem!")
i = int(input("Inicio: "))
f = int(input("Fim: "))
p = int (input("Passo: "))
Contador(i, f, p)
#fim
