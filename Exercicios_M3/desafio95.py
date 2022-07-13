#Al: Aprimoramento do exercicio 93, para que funcione com vários jogadores,
# incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador
#autor: Lucas Borguezam
#data:

#Import

#Inicio
jogadores = list()
dados = dict()
gols = list()
#Cadastrando dados ---------------------------------------------------
while True:
    dados.clear()
    gols.clear()
    dados["nome"] = str(input("Atleta: ")).title()
    partidas = int(input("Número de partidas Jogadas: "))
    #a

    totgol = 0
    for c in range(0, partidas):
        gols.append(int(input(f"quantidade de gols na {c+1}° Partida: ")))
        totgol += gols[c]
    dados["gols"] = gols[:]
    dados["total"] = totgol
    jogadores.append(dados.copy())
    while True:
        cond = str(input("Quer Continuar? [S/N]")).strip().upper()[0]
        if cond in 'SN':
                break
        else:
            print("Erro!! Digite 'S' ou 'N'.")
    if cond == 'N':
        break
print("-="*50)
#----------------------------------------------------------------------
#Mostrando dados ---------------------------------------------------
print("Cod ", end='')
for i in dados.keys():
    print(f"{i.title():<15}", end='')
print()
print('-' * 40)
for c, i in enumerate(jogadores):
    print(f"{c:>3} ", end='')
    for d in i.values():
        print(f"{str(d):<15}", end='')
    print()
#----------------------------------------------------------------------
# Mostrando dados que o usuário pede ---------------------------------------------------
while True:
    busca = int(input("Mostrar dados de qual Jogador? "))
    if busca == 999:
        break
    elif busca >= 0 and busca < len(jogadores):
        print(f"-- levantamento do Jogador {jogadores[busca]['nome']}")
        for i, g in enumerate(jogadores[busca]['gols']):
            print(f"No jogo {i+1} fez {g} gols.")
    else:
        print(f"ERRO! Não existe jogador com esse código {busca}!")
    while True:
        op = str(input("Deseja Continuar? [S/N] ").upper().strip()[0])
        if op in 'SN':
            break
        else:
            print("Erro! Digite S ou N")
    if op == 'N':
        break
print('-'*50)
print("<< Volte Sempre >>")
#FIM-------------------------------------------------------------------
