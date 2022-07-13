#Al: leia um numero real, coverter para dolar
#autor: Lucas Borguezam
#data:08032022

# considere U$=1.00 == R$3.27

#variáveis
dinehiro = 0.0
convertido = 0.0
#Inicio
dinheiro= float(input('Quanto Dinheiro você tem na carteira? R$'))
convertido = dinheiro/3.27
print('O valor {:.2f}R$, equivale a: {:.2f}U$'.format(dinheiro, convertido))
#ou
print('O valor {:.2f}R$, equivale a: {:.2f}U$'.format(dinheiro, dinheiro/3.27))

#Fim.