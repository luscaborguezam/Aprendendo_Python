#Al:Programa que recebe velocidade do carro, se o carro passar de 80 Km/h acrescentar multa de 7,00 por km
#autor: Lucas Borguezam
#data:18032022

#Import

#Inicio
velo= float(input("Qual sua velocidade: "))

print(
    'Velocidade limite respeitada'if velo<80.00
    else'Multa de R${} por excesso de velocidade'.format((velo-80.00)*7.00)
    )

#fim
