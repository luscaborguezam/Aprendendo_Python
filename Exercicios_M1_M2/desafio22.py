                  #Al: Programa que leia um nome que leia o nome completo de uma pssoa e mostre:
# 1-nome com todas as letras maiusculas
# 2-todas minusculas
# 3-quantas letras no total (sem considerar espaços)
# 4-Quantas letras tem o 1°nome
#autor: Lucas Borguezam
#data:18032022

#Import

#Inicio
nome = str(input("Nome: ")).strip()

#print("Caixa alta: {}\n/Caixa baixa: {}\nN° letras:{}\nNº letras 1° nome:{}".format(nome.upper(), nome.lower(), len(nome.replace(" ","")), len(nome.split()[0])))
print("Seu nome em Maiúculas é {}".format(nome.upper()))
print("Seu nome me minúsculas é {}".format(nome.lower()))
print("seu nome tem ao todo {} letras".format(len(nome.replace(" ",""))))
print("Seu primeiro nome tem {} letras".format(len(nome.split()[0])))

print("\nOU correção:\n")

print("Seu nome em Maiúculas é {}".format(nome.upper()))
print("Seu nome me minúsculas é {}".format(nome.lower()))
print("seu nome tem ao todo {} letras".format(len(nome) - nome.count(' ')))
#len: conta todos os caracteres existentes na variável - count: conta todos caracteres especificados existentes na variável que é o: " "
print("Seu primeiro nome tem {} letras".format(nome.find(" ")))
#find encontra a localização do caracter especificado:" ".
#obs: O python sempre mostra um numero antes do caracter especificado. ex: Lucas G find(" ")==5 mas ele ocupa a posição 6

#fim