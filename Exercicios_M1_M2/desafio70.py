#Al: Leia nome e preço de n produtos, programa pergnta se o usuário quer continuar, e mostrar total gasto,
# quantos produtos acima de 1000 e nome do produto mais barato
#autor: Lucas Borguezam
#data:

#Import
total = 0
PCaros = 0
cont = 0
nomeM = ""
#Inicio
while True:
    print(f"{'-'* 10}Produtos da Campra{'-'*10}")
    nome = str(input("nome do produto: ").strip())
    preco = float(input("Preço: ").strip())
    #acumulador
    total += preco
    #Produtos acima de 1000
    if preco > 1000:
        PCaros += 1
    #Produto mais barato
    if cont == 0 or preco < menor:
        menor = preco
        nomeM = nome
        cont =+1
    #condição de parada
    condicao = ""
    while condicao not in 'SN':
        condicao = str(input("Deseja continuar?[S/N] ").upper().strip()[0])
    if condicao == "N":
        break
print(f'Total Gasto R${total:.2f}\n'
      f'Produtos acima de R$1000.00: {PCaros}\n'
      f'Produto mais barato: {nomeM} que custa R${menor:.2f}')

#fim
