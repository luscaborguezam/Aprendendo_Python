#Al: refazendo exercicio 009 com for
#autor: Lucas Borguezam
#data:

#Import

#Inicio
#variáveis
n=0
#Inicio
n=int(input('Digite um numero para saber sua tabuada: '))
print('_'*12)
for t in range(0, 11):
    print("{}X{}={}".format(n, t, n*t))

print('_'*12)

#fim
