#Al:Programa que peça nome e peso para varias pessoas, guarde em uma lista. E mostre:
# Qtd pessoas cadastradas
# lista de pessoas mais pesadas
# lista de pessoas mais leves
#autor: Lucas Borguezam
#data:

#Import

#Inicio
pessoas = list()
dados = list()
while True:
    dados.append(str(input("Nome: ")))
    dados.append(float(input("Peso: Kg")))
    if len(pessoas) == 0:
        maior = menor = dados[1]
    elif dados[1] > maior:
        maior = dados[1]
    elif dados[1] < menor:
        menor = dados[1]
    pessoas.append(dados[:])
    dados.clear()
    cond = str(input("Deseja continuar? [S/N]").strip().upper()[0])
    if cond == 'N':
        break
print(pessoas)

print(f"Ao todo foram cadastrados {len(pessoas)} pessoas\n"
      f"O maior peso foi de {maior:.1f}kg. Peso de ", end='')
for c in pessoas:
    if c[1] == maior:
        print(c[0], end= ' ')
print("\n"
      f"O menor peso foi de {menor:.1f}kg. Peso de ", end='')
for c in pessoas:
    if c[1] == menor:
        print(c[0], end=' ')
#fim
