#Al: Programa que recebe valor em km, calculando 0,50R$ por km caso seja viajens de até 200km,
# se for maior, 0,45R$ por km
#autor: Lucas Borguezam
#data:07/04

#Import

#Inicio
km = float(input("Qual a distancia(KM)? "))
print("___Viajem___")
# print("Classificação: Viagem curta\nValor: R${}".format(km*0.50)if km<200
#       else"Classificação: Viagem Longa\n valor: R${}".format(km*0.45)
# ou
preco = km * 0.50 if km<=200 else km * 0.45
print("O Preço da sua passagem será R${:.2f)".format(preco))
#fim
