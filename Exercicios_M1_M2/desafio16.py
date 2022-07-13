#Al: leia um numero real e mostre sua porção inteira
#autor: Lucas Borguezam
#data:16032022

#importações
from math import trunc
#variáveis
n=0.0
#Inicio
n =float(input("Digite um numero Real "))
print("A parte inteira de {} é: {}".format(n, trunc(n))) # ou floor
#fim

#ou
'''
#variáveis
n=0.0
#Inicio
n =float(input("Digite um numero Real "))
print("A parte inteira de {} é: {}".format(n, int(n)))
#fim
'''
#ou
'''
#importações
import math
#variáveis
n=0.0
#Inicio
n =float(input("Digite um numero Real "))
print("A parte inteira de {} é: {}".format(n, math.trunc(n)))
#fim
'''


