#Al: ler .5 pesos e informar o maior e o menor
#autor: Lucas Borguezam
#data:

#Import

#Inicio

for pessoa in range(1, 6):
    peso = float(input("Qual o peso da {}° pessoa? ".format(pessoa)))
    if pessoa == 1:
        maior = peso
        menor = peso
    elif peso > maior:
        maior = peso
    elif peso < menor:
        menor = peso
print("O menor peso é {}Kg \nO maior peso é {}Kg".format(menor, maior))


#fim
