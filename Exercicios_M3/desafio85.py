#Al: Programa que recebe 7 valores numéricos em uma lista,que separe os valores pares de impares,
# no finmal mostrar: valores pares e impares em  ordem crescentea
#autor: Lucas Borguezam
#data:
all = [[], []]# todos
#Import

#Inicio
for c in range(0, 7):
    v = int(input(f"Digite o {c+1}° valor: "))
    if v%2==0:
        all[1].append(v)
    else:
        all[0].append(v)
all[1].sort()
all[0].sort()
print(f"Os valores pares digitados são: {all[0]}\n"
      f"Os valores ímpares digitados são: {all[1]}")
#fim
