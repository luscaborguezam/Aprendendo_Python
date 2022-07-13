#Al:leia n valores com parada no 999, mostrar a soma dos valores digitados e quantos valores foram figitados
#autor: Lucas Borguezam
#data:

#Import

#Inicio
i = acu = v =0

while True:
    v = int(input("Digite o valor desejado(código de parada 999)"))
    if v == 999:
        break
    i += 1
    acu += v
print(f"A soma é {acu} de {i} números digitados")
#fim
