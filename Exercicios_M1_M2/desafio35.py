#Al: Programa que recebe 3 comprimentos e mostra possibilidade de formar um triangulo
#autor: Lucas Borguezam
#data:

#Import

#Inicio
print("--"*20)
print("Calculadora de existencia de Treiângulo")
print("--"*20)
a = int(input("Primeiro segmento: "))
b = int(input("Segundo segmento: "))
c = int(input("Terceiro segmento: "))

#Condição de existencia de um triangulo, se a soma de dois segmentos for maior que o terceiro ele pode existir

if (a+b)>c and (b+c)>a and (a+c)>b:
    print("É possível formar um triângulo")
else:
    print("Impossível formar um triângulo.")


#fim
