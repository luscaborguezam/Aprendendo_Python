#  import importar bibliotecas
# import biblioteca
# ou posso importar algo especifico
# from biblioteca import
#math - matematica
#import math
#from math import ceil #arredondamento para cima
# Funcionalidades dp math
#floor arredondamento para baixo
#trunc pega só a parte inteira dispensando os numeros após a ','
#pow potencia
#sqrt raiz quadrada
#factorial fatorial

#import math
from math import sqrt, floor

num=int(input("Digite um numero: "))
raiz = sqrt(num)
print("Raiz do {} é igual a {}".format(num, floor(raiz)))

import random #gera numeros aleatórios
num = random.random() #numero reais entre 0 e 1
num2= random.randint(1, 10) #numero inteiro entre 1 e 10

import emoji
print(emoji.emojize("olá mundo? :earth_americas:", use_aliases=True)) # usar o site para ver os nomes dos emojis
