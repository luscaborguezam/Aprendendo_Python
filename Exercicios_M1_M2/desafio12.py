#Al: leia um valor, e mostre o valor com 5% de desconto
#autor: Lucas Borguezam
#data:08032022

#variáveis
v=0.0
d=0.0
vd=0.0
#Inicio
v= float(input('Preço do produto? R$'))
d = v*0.05 # ou (v*5)/100
vd = v-d
print('Valor: {}\nDeconto: {}\nValor Final: {}'.format(v, d, vd))
#Fim.