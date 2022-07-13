#Variável Composta
# Diferente da tupla a lista(array) é mutavel
num = [2, 5, 9, 1]
print(num)
num[2] = 3
print(num)
# Array[]
# alguns comandos são siferentes
lanches = ["Hamburguer", "Suco", "Pizza", "Sorvete"]
print(lanches)
#adicionando item
print("\033[1;32mAdicinando com append o item 'Cokie' a lista\033[m")
lanches.append("Cookie")
print(lanches)
#adiciona item em uma posição especifica
print("\033[1;32mAdicinando com insert o item 'Cachorro Quente' na posição 0\033[m")
lanches.insert(0, "Cachorro Quente")
print(lanches)
#deletando itens
    #procura pelo index
print("\033[1;31mDeletando item no índice 3\033[m")
del lanches[3]
print(lanches)
    #ou
    # utilizado para eliminar o ultimo item, mas se passar o parametro funciona igual ao del
print("\033[1;31mDeletando item no índice 1 pelo método pop\033[m")
lanches.pop(1)
print(lanches)
    #procura pelo conteudo e remove
print("\033[1;31mDeletando item pelo conteudo 'Sorvete'\033[m")
lanches.remove('Sorvete')
print(lanches)

#---------Criando lista com range
valores = list(range(4,11))
print(f"\033[1;32mCriando valores em uma lista Com list(range(4,11)):\033[m \n{valores}")

print("\033[1;36m Manipulando as ordens das listas\033[m")
numeros = [8, 2, 5, 4, 9, 3, 0]
print(f"Lista: {numeros}")
# Ordenando lista método sort
numeros.sort()
print(f"ordenando os valores método .sort(): {numeros}")
    #ordem inversa com parametro (reverse=True)
numeros.sort(reverse=True)
print(f"ordenando os valores na ordem reversa com o .sort(reverse=True): {numeros}")
print(f"Valores na lista com len(lista): {len(numeros)}")

for c, v in enumerate(numeros):
    print(f"Na posição {c} encontrei o valor {v}")
print("Fim da lista")
print("-="*20)#-=--- Igualdade em listas
a = [2, 3, 4, 7]
b = a
print(f"A={a}\nB={b}")
print("b[2] = 8")
b[2] = 8
print(f"lista A:{a}\nlista B:{b}")
print("Ao igualar uma lista 'b = a' o python cria uma ligação entre elas. "
      "\nPor isso ao mudar a lista B mudou tâmbem a lista A ")
print("Método para copiar uma lista sem ligação é:"
      "\nc = a[:] #C recebe todos itens de A")
c = a[:]
print(f"C:{c}\nA:{a}")
print("c[2] = 9")
c[2] = 9
print(f"C:{c}\nA:{a}")