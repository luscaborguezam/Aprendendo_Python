#Al: Aprimorando o desafio anterior, mosttrando no final:
#A) a soma de todos valores pares
#B) soma da terceira coluna
#C) Maior valor da segunda coluna
#autor: Lucas Borguezam
#data:

#Import

#Inicio
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somap = somac = maior = 0

for l in range(0, 3):
    for c in range(0,3):
        matriz[l][c] = int(input(f"Digite um valor para [{l}, {c}]: "))

for linhas in matriz:
    for colunas in linhas:
        print(f"[ {colunas:^5} ]",end='')
    print()

for l in range(0,3):
    for c in range(0,3):
        if matriz[l][c]%2==0:
            somap += matriz[l][c]
        if c == 2:
            somac += matriz[l][c]
        if l == 1:
            if c == 0:
                maior = matriz[l][c]
            elif maior < matriz[1][c]:
                maior = matriz[l][c]

print(f"Soma dos valores pares é {somap}\n"
      f"Soma da 3° coluna é {somac}\n"
      f"MAior valor 2°linha é: {maior}")
#fim
