#Al: Leia 3 numeros e mostre o maior e o menor
#autor: Lucas Borguezam
#data:07/04

#Import

#Inicio
a = int(input("Escreva um valor"))
b = int(input("Escreva outro valor"))
c = int(input("Escreva outro valor"))
#verificando menor valor
menor = a
if b<a and c>b:
    menor = b
if c<a and b>c:
    menor = c
#maior valor
maior = a
if b>a and c<b:
    maior = b
if c>a and b<c:
    maior = c

print("O MENOR valor digitado foi {}".format(menor))
print("O MAIOR valor digiado foi {}".format(maior))

#fim
