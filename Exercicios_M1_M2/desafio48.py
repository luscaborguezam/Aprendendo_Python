#Al: soma de numeros entre 1 e 500 que são impares e multiplos de 3
#autor: Lucas Borguezam
#data:

#Import

#Inicio
soma = 0 #acumulador
cont1 = 0 #contador
for c in range(1, 500+1):
    if (c % 2 == 1) and (c%3 == 0):
        soma += c
        cont1 += 1
print("A soma dos valores solicitados é {}.\nQuantidade de Números somados= {}".format(soma, cont1))

# or (processamento é menor que a forma anterior)
soma2 = 0 #acumulador
cont2 = 0 #contador
for n in range(1, 501, 2):
    if n % 3 == 0:
        soma2 = soma2 + n
        cont2 += 1
print("A soma dos valores solicitados é {}.\nQuantidade de Números somados= {}".format(soma2, cont2))
#fim
