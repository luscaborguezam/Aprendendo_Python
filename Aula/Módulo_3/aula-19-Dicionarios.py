# Variavel Composta
# É Mutavel
# identificados pelas {} 'chaves'
# Permite ter indices Literais. Personalizar os indices
dados = dict()
dados = {'nome':'Pedro', 'idade':25}
print(dados)
print(f"print(dados[nome])-> {dados['nome']}")
print(f"print(dados['idade'])-> {dados['idade']}")
#append não funcionar
# para adicionar elementos é assim:
print("\033[1;32mAdicionando dados com o:\033[m\n"
      "dados['sexo'] = 'M'")
dados['sexo'] = 'M'
print(dados)
#removendo dados com o del e o nome do indice
print("\033[1;31mDeletando dados com o:\n\033[m"
      "del dados['idade']")
del dados['idade']
print(dados)
#outra forma de criar
filme = {
    'titulo':'Star Wa rs',
    'ano':1977,
    'diretor':'George Lucas'
}
print("\nImportante saber a diferença entre valores, chaves, item")
print(filme)

print("\nalores ficam depois dos ':'")
print(filme.values())
print("\nsão as chaves, os indices personalizados")
print(filme.keys())
print("\nPega tanto as chaves e o valor")
print(filme.items())
print()
for k, v in filme.items():
    print(f'O {k} é {v}')

print("Podemos mesclar as estruturas ex: ")

locadora=list()
locadora = (
    {
    'titulo':'Star Wars',
    'ano':1977,
    'diretor':'George Lucas'
    },
    {
    'titulo':'Avengers',
    'ano':2012,
    'diretor':'Joss Whedon'
    },
    {
    'titulo':'Matrix',
    'ano':1999,
    'diretor':'Wachowski'
    }
)
print(locadora)
print("chaves  da locadora item 0:")
print(locadora[0].keys())


print()

estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input("Unidade Federativa: "))
    estado['sigla'] = str(input("Sigla do Estado: "))
    brasil.append(estado.copy()) #Para adicionar dicionário como itens a uma lista sem criar uma ligação usa o 'copy()'
print(brasil)
for e in brasil:
    for k, v in e.items():
        print(f"{k}:{v}]")
    print()


print()
# adicionando um dicionário a outro
D1 = {"Nome":"luc","Pais":"USA"}
D2 = {"firstname":"justin","lastname":"lambert"}
D1.update(D2)
print(D1)