#Al: Leia nome, numero de partidas jogadas, quantidade de gols feitos em cada partida
#autor: Lucas Borguezam
#data:

#Import

#Inicio
dados = dict()
dados["nome"] = str(input("Atleta: ")).title()
partidas = int(input("Número de partidas Jogadas: "))
gols = list()
totgol = 0
for c in range(0, partidas):
    gols.append(int(input(f"quantidade de gols na {c+1}° Partida: ")))
    totgol += gols[c]
dados["gols"] = gols[:]
dados["total"] = totgol
print("-="*50)
print(dados)
print("-="*50)
for k, v in dados.items():
    print(f'O campo {k} tem o valor {v}')
print("-="*50)
print(f"O jogador {dados['nome']} jogou {partidas} ")
for c, i in enumerate(dados["gols"]):
    print(f"    => Na Partida {c+1}, fez {i} gols")
print(f'Foi um total de {dados["total"]} gols.')
#fim
