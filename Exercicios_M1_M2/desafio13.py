#Al: leia um salário, e mostre o valor com 15% de aumento
#autor: Lucas Borguezam
#data:08032022

#variáveis
s=0.0
a=0.0
sa=0.0
#Inicio
s=float(input('Qual o salário do Funcionário? R$'))
a=s*0.15#ou ((s*15)/100)
sa=s+a
print('O salário: {:.2f}R$, com aumento de 15% passou a ser: {:.2f}R$'.format(s, sa))
#Fim.