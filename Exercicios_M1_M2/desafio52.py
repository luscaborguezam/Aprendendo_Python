#Al: Programa que diz se o numero informado é primo
#autor: Lucas Borguezam
#data:

#Import

#Inicio
n = int(input(print("Digite um número que deseja saber se ele é primo: ")))
cont =0
for c in range(1, n + 1):
    #diferenciando os números divisiveis
    if n % c == 0:
        print("\033[32m", end=" ")
        cont += 1
    else:
        print("\033[31m", end=" ")
    print("{}".format(c), end=" ")
# mostrando os números divisíveos
print('\033[mnúmero {} foi divisível {} vezes'.format(n, cont))
# definindo se é Primo ou não
if cont == 2:
    print("E por isso ele é PRIMO")
else:
    print("E por isso ele não é PRIMO")
#fim
