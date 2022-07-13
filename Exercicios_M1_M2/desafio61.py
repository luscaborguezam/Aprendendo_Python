#Al: exercicio 51, com while
#autor: Lucas Borguezam
#data:

#Import

#Inicio
# primeiro = int(input(print("1° Termo: ")))
# razao = int (input(print("Razão: ")))
# decimo = primeiro + (10 - 1) * razao
#
# while primeiro <= decimo:
#     print("{}".format(primeiro))
#     primeiro += razao
# print("Acabou!")

#correção
primeiro = int(input(print("1° Termo: ")))
razao = int (input(print("Razão: ")))
termo = primeiro # termo começa com o primeiro termo
cont = 1

while cont <= 10:
    print('{} -> '.format(termo), end='')
    termo += razao
    cont += 1
print("fim")
#fim
