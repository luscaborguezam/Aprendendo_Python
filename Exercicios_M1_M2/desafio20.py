
#Al: leia 4 nomes e mude a ordem de apresentação de forma aleatória
#autor: Lucas Borguezam
#data:18032022

#Import
from random import shuffle
#Inicio
n1 = str(input("1° nome: "))
n2 = str(input("2° nome: "))
n3 = str(input("3° nome: "))
n4 = str(input("4° nome: "))

lista = [n1,n2,n3,n4]
shuffle(lista)#shuffle embaralha a lista
print(lista)

#fim