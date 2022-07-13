#Al: leia um angulo e mostre ovalor de seno cosseno e tangente
#autor: Lucas Borguezam
#data:16032022

#importe

from math import radians, sin, cos, tan
#Variaveis
a=0.0
seno=0.0
cosseno=0.0
tangente=0.0
#inicio
a = float(input("Digite o ângulo que você : "))
#radians transforma o numero informado em radiano.
seno= sin(radians(a)) #sin calcula o seno
cosseno = cos(radians(a))#cos calcula o cosseno
tangente = tan(radians(a))#tan calcula a tangente

print('O angulo de {} tem SENO de {:.2f}'.format(a, seno))
print('O angulo de {} tem COSSENO de {:.2f}'.format(a, cosseno))
print('O angulo de {} tem a TANGENTE de {:.2f}'.format(a, tangente))

#fim.