#Al: Receba 4 nomes e escolha um aleatóriamente
#autor: Lucas Borguezam
#data:18032022

#Import
from random import choice
#Inicio
n1 = str(input("Digite o 1° nome: "))
n2 = str(input("Digite o 2° nome: "))
n3= str(input("digite o 3° nome: "))
n4= str(input("digite o 4° nome: "))
lista = [n1, n2, n3, n4]
escolhido = choice(lista) #'choice' uma escolha dentro da (lista)
print("O nome sorteado é {}.".format(escolhido))
#fim