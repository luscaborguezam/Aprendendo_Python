#Al: Programa que calcule se o numero recebido é par ou impar
#autor: Lucas Borguezam
#data:07/04

#Import

#Inicio
n = str(input("Digite um numero para saber se é par ou impar: "))

if (n.isnumeric()):
    n = int(n)
    # q = int(n/2)
    # r = n - (q*2)
    print('Par'if n%2==0 else'Impar')
else:
    print("Valor inválido, Digite um número")
#fim
