import random #ou from random import randint
a = random.randint(0, 10) # número aleatórios de 0 a 10

import math
b = math.factorial(7)

from datetime import datetime #ou import datetime
x = datetime.now().year # Recebendo ano atual da máquina

from operator import itemgetter #usado para pegar itens especificos de um dicionário como em uma lista, e trasformando em uma lista
posicoes = {'Player1':7, 'Player2':3, 'Player3':5, 'Player4':8, 'Player5':13, 'Player6':2}
ranking = sorted(posicoes.items(), key=itemgetter(1), reverse=True)
print(ranking)
# sorted = ordena uma lista, reverse coloca ela na ordem reversa.

import urllib # com ela consigo verificar se o computador consegue acessar o site.
import urllib.request
site = 'http://pudim.com.br'
conection = urllib.request.urlopen(site)
