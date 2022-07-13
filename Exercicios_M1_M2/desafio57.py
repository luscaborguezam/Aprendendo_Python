#Al: Programa que le valores "M" ou "F" caso esteja errado pedir que gdigite novamente
#autor: Lucas Borguezam
#data:

#Import
from time import sleep
#Inicio
# condicao = ""
# while condicao != "M" and condicao != "F":
#     condicao = input("Qual seu sexo [M/F]?\n").strip().upper()[0]
#     if condicao != "M" and condicao != "F":
#         print("Opção inválida\nDigite novamente!!")
#         sleep(0.5)
# print("fim")

#Correção:

sexo = str(input("Digite seu sexo: [M/F]")).strip().upper()
while sexo not in 'MmfF':
    sexo = str(input("Dados inválidos. Por favor, informe seu sexo: ")).strip().upper()
    sleep(0.5)
print("Sexo {} cadastrado com sucesso!".format(sexo))

#fim
