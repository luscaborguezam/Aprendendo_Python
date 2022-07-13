#Al: ler quatro valores e guardar em uma tupla.
#       Mostrar quantas vezes apareceu o valor 9
#       Em que posição está o primeiro 3
#      Mostrar os números pares
#autor: Lucas Borguezam
#data:

#Import

#Inicio
numeros = (int(input("Digite um número: ")), int(input("Digite um número: ")), int(input("Digite um número: ")),
           int(input("Digite um número: ")))
print(f"Você digitou os valores {numeros}")
print(f"O Valor 9 apareceu {numeros.count(9)} vezes")
if 3 in numeros:
    print(f"O valor 3 está na posição {numeros.index(3)} pela primeira vez")
else:
    print("Nenhum número 3 encontrado")
print("Valores pares encontrados: ")
for n in numeros:
    if (n % 2) == 0:
        print(n, end=' ')

#fim
