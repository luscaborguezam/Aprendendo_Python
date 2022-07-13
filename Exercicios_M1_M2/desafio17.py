#Al: leia cateto oposto e adjacente e calcule a hipotenusa
#autor: Lucas Borguezam
#data:16032022

#Importações
from math import hypot
#variáveis
co=0.0
ca=0.0
hip=0.0
#Inicio

co = float(input("Cateto oposto: "))
ca = float(input("Cateto adjacente: "))

'''hip= (co**2+ca**2)**(1/2)'''
# ou
hip = hypot(co, ca)
print("a hipotenuza é: {:.2f}".format(hip))
#fim