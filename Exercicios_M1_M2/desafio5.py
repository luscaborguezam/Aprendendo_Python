#Faça um prgrama que leia um número inteiro e mostre o seu sucessor e seu antecessor
x = int(input('Digite um numero: '))
a = int(x-1)
s = int(x+1)
print('O sucessor é {} e o antecessor é {}'.format(s, a))

# Correção fez (pois não terá de usar o sucessor e o antecessor depois)
n = int(input('Digite um numero: '))
print('Análisando o valor {}, seu sucessor é {} e o antecessor é {}'.format(n, n+1, n-1))