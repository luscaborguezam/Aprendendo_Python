#Al:Função maior, recebr vários valores, e ao fimmostrar o maior.
#autor: Lucas Borguezam
#data:

#Import
from time import sleep
#Inicio


def Maior(* numeros):
    if len(numeros) == 0:
        maior = 0
    print("-="*30)
    print("Analisando os valores passados...")
    print(f"Foram informados {len(numeros)} valores ao todo")
    for c, n in enumerate(numeros):
        print(n, end=' ', flush=True)
        sleep(0.3)
        if c == 0:
            maior = n
        if maior < n:
            maior = n
    print(f"O maior valor é {maior}")
Maior(2, 9, 4, 7, 1)
Maior(4, 7, 0)
Maior(1, 2)
Maior(6)
Maior()
#fim
