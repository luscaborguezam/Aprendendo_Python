#Al: Programa que elia um numero de 0 a 9999 e mostre cada um ods digitos separados
#ex: 1834
# Unidade:4
# Dezena:3
# centena:8
# milhar:1
#autor: Lucas Borguezam
#data:18032022

#Import

#Inicio
numero = str(input("Digite o numero entre 0 e 9999\n")).strip()
numero = numero.replace(" ","")
print("Analisando {}\nUnidade:{}\nDezena:{}\nCentena:{}\nMilhar:{}".format(numero,numero[0], numero[1], numero[2], numero[3]))

#ou

u = numero// 1 % 10
d = numero// 10 % 10
c = numero// 100 %10
m = numero// 1000 %10
print("Analisando {}\nUnidade:{}\nDezena:{}\nCentena:{}\nMilhar:{}".format(numero,u, d, c, m))

#fim