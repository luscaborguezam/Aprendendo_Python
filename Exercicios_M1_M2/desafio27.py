#Al:Programa que receba o nome completo, e mostre o primeiro e o ultimo nome separadamente
#autor: Lucas Borguezam
#data:18032022

#Import

#Inicio
nome = str(input("Digite seu nome: ")).strip().split()

print("Seu primeiro nome é {}".format(nome[0]))
print("Seu ultimo nome é {}".format(nome[len(nome)-1]))
#fim
