#Variável Composta
# Diferente da tupla a lista(array) é mutavel
# Listas dentro de listas

listaTotal = list()
listaTotal = [['Pedro', 25], ['Maria', 19], ['Jão', 32]]
print(listaTotal)
print("lista[0] de listaTotal, item [0] da lista[0] interna\n"
      f"listaTotal[1][0]: {print(listaTotal[0][0])}", end='')
print("lista[1] de listaTotal, item [1] da lista[1] interna\n"
      f"listaTotal[1][1]: {print(listaTotal[1][1])}", end='')
print("lista[2] de listaTotal, item [0] da lista[2] interna\n"
      f"listaTotal[2][0]: {print(listaTotal[2][0])}", end='')
print("\n","**--"*20)

teste = list()
teste.append('Gustavo')
teste.append(40)
galera = list()
print("\033[1;31m Se não usar '[:]' ao adicionar uma lista a uma variável, é criado uma conexão.\033[m")
galera.append(teste[:])
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])

galera = [['Gustavo', 40], ['Maria', 22], ['Julli', 19], ["Joaquin", 13]]
print(galera)
for c in galera:
    print(f"Nome: {c[0]}, Idade: {c[1]}")
print("\n\n"
      "Recebendo valores em uma lista e salvando a lista dentro de outra:")
galera = list()
dado = list()
for c in range(0, 3):
    #Adciono item nome e idade na lista dado
    dado.append(str(input("Nome: ")))
    dado.append(int(input("Idade: ")))
    #adiciono a lista dado para lista pessoas
    galera.append(dado[:])
    #limpo a lista dado
    dado.clear()
print(galera)

print("\n"
      "Mostrando dados com a condição idade > 19")
totmai = totmen = 0
for c in galera:
    if c[1] > 19:
        print(f"{c[0]} é maior de idade")
        totmai+=1
    else:
        print(f"{c[0]} é menor de idade")
        totmen+=1
print(f"Temos {totmai} maiores e {totmen} menores")
#fim
