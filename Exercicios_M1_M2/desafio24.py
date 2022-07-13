#Al:Programa que receba o nome de uma cidade e diga se ela começa com nome "SANTO"
#autor: Lucas Borguezam
#data:18032022

#Import

#Inicio
nome = str(input("Nome da cidade em que mora: ")).strip()
#correção
print(nome[:5].upper() == "SANTO")
# n1 = nome.find(" ")
# if (nome[:n1].upper() == "SANTO"):
#     print("Nome da sua cidade Começa com 'Santo'")
# else:
#     print("Nome da sua cidade não começa com 'SANTO'")

#ou
# print("A cidade {} começa com SANTO?\nResposta:{}".format(nome, "SANTO" in nome.upper()))


#if ()
#fim