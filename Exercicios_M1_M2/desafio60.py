#Al: fatorial
#autor: Lucas Borguezam
#data:

#Import
from math import factorial
#Inicio
#Resolução

# i = int(input("Digite o número que deseja.\n>>"))
# n1 = i
# a = i
# while i > 1:
#     a *= (i - 1)
#     i -= 1
# print("O fatorial de {} é {}".format(n1, a))

#Correção
n = int(input("Digite o número que deseja.\n>>"))
c = n # contador
f = 1 # igaul a 1 por se tratar de uma multiplicação
print("O fatorial de {}! = ".format(n), end="")
while c > 0:
    print("{} ".format(c), end='')
    print('X ' if c > 1 else '= ', end='')
    f *= c
    c-= 1
print("{}".format(n, f))

# #solução mais simples
# n = int(input('Digite um número para calcular o fatorial: '))
# print('O fatorial de {} é {}'.format(n, factorial(n)))

# Desafio com o laço for
n = int(input("Digite o número que deseja:\n"))
f = 1# fatorial
print("{}! = ".format(n), end='')
for c in range(n , 0, -1):
    print("{}".format(c), end="")
    print(" X " if c > 1 else ' = ', end='')
    f *= c
print("{}".format(f))
#fim
