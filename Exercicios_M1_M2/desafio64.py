#Al:leia n numeros inteiros, condição de parada é 999, mostre no final quantos numeros foram digitados e qual
# a soma deles
#autor: Lucas Borguezam
#data:

#Import

#Inicio
i = 0
a = 0
c = 0
i = int(input("Digite um número: "))
while i != 999:
    a += i
    c += 1
    i = int(input("Digite um número: "))
print("Você digitou {} números\nA soma deles é: {}".format(c, a))
#fim
