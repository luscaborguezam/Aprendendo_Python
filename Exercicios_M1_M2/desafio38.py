#Al: Programa rebcebe dois numeros inteiros e cmpare mostrando o maior ou mostre que são iguais
#autor: Lucas Borguezam
#data:21/04/2022

#Import

#Inicio
n1=int(input("1° valor: "))
n2=int(input("2° valor: "))

if n1>n2:
    print("O 1° valor é o maior")
elif n2>n1:
    print("O 2° valor é o maior")
else:
    print("Não existe valor maior, os dois são iguais")
#fim
