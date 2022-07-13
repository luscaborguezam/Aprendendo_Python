#Al: Soma de 6 numeros digitados pelo usuário, somando apenas se for par
#autor: Lucas Borguezam
#data:

#Import

#Inicio
soma = 0
cont = 0
for c in range(1, 7):
    n = int(input(print("Digite um Número")))
    if n % 2 == 0:
        soma += n
        cont += 1
print("Soma dos {} números pares digitado é: {}".format(cont, soma))



#fim
