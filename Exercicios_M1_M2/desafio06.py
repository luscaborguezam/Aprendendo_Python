#crie um algoritimo que leia um numero e mostre o seu dobro triplo e raiz quadrada
#Al: leia um numero e calcule seu dobro, triplo e raiz quadrada

# Variáveis
n=0
d=0
t=0
r=0.0
#Inicio
n = int(input('Digite um número '))
d = n*2
t = n*3
r = n ** (1/2)

print('O dobro de {} é: {}, o triplo: {}, raiz quadrada: {:.2f}.'.format(n, d, t, r))
#Fim.

#ou em caso de usar o minimo de variáveis , a fim de fazer o que se pede sem um uso das informações posteriormente.
print('O dobro de {} é: {}, o triplo: {}, raiz quadrada: {:.2f}.'.format(n, (n*2), (n*3), (n**(1/2))))

print('raiz quadrada usando pow: {:.2f}.'.format(pow(n, (1/2))))