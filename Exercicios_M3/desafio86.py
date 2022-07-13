#Al: Programa q crie uma matriz, e preencha os valores lidos pelo teclado, mostrar
# formação correta da matriz
#autor: Lucas Borguezam
#data:

#Import

#Inicio
matriz=[[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for x in range(0,3):
    for y in range(0, 3):
        matriz[x][y] = (int(input(f"Digite um valor para a posição [{x}, {y}]: ")))

for linhas in matriz:
    for colunas in linhas:
        print(f"[{colunas:^5}]",end='')
    print()
#fim
