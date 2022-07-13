#Al: Programa que calcule o IMC, mostrando o status de acordo com: 18.5 abaixo do peso, 18.5 a 25 peso ideal,
# 25 a 30: sobrepeso, 30 a 40 obesidade, acima de 40 obesidade mórbida
#autor: Lucas Borguezam
#data:

#Import

#Inicio
peso = float("Digite seu peso ")
altura = float("Digite sua altura ")

IMC = peso /(altura**2)
if IMC < 18.5:
    print("Você está abaixo do peso")
elif IMC <= 25:
    print("Você esta no peso ideal")
elif IMC <= 30:
    print("Você esta no sobrepeso")
elif IMC <= 40:
    print("Você está na obesidade")
else:
    print("Vocé está na OBESIDADE MÓRBIDA")
#fim
