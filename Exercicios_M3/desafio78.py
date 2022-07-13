#Al: Leia 5 valores e guarde em uma lista, mostrar qual o maior e o menor valor digiado
# e suas respectivas posições na lista
#autor: Lucas Borguezam
#data:

#Import

#Inicio
valores=[]
for v in range (0, 5):
    valores.append(int(input(f"Digite oum valor para a Posição {v}: ")))
    if v == 0:
        maior = menor = valores[v]
    else:
        if maior < valores[v]:
            maior = valores[v]
        elif menor > valores[v]:
            menor = valores[v]
print("=-"*20)
print(f"Valores digitados:{valores}")
print(f"Maior valor: {maior} ocupa a posição {valores.index(maior)}")
print(f"Menor valor: {menor} ocupa a posição {valores.index(menor)}")

# ou
print(f"{'ou':^20}")
print(f"Maior valor digitado: {maior}, nas posções: ", end='')
for con, v in enumerate(valores):
    if v == maior:
        print(f'{con}... ', end='')
print(f"Menor valor digitado: {menor}, nas posções: ", end='')
for con, v in enumerate(valores):
    if v == menor:
        print(f'{con}... ', end='')
#fim
