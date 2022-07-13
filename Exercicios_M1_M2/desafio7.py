#ler dois valores calcular média
#autor: Lucas Borguezam
#08/03/2021

#variáveis
n1=0.0
n2=0.0
m=0.0
#Inicio
n1=float(input('Digite a primeira nota '))
n2=float(input('Digite a segunda nota '))

m= (n1+n2)/2

print('O valor da média entre {:.1f} e {:.1f} é: {:.1f}.'.format(n1, n2, m))

# ou

print('O valor da média entre {:.1f} e {:.1f} é: {:.1f}.'.format(n1, n2, ((n1+n2)/2)))

#Fim.