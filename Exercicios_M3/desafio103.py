#Al: Função Ficha(), receba parâmetro nome e gols
#autor: Lucas Borguezam
#data:

#Import

#Inicio


def Ficha(nome='', gols=''):
    if nome.strip() == '':
       nome = "<desconhecido>"
    if gols.strip() == '':
        gols = 0
    """
    ->Registra dados de um jogador como uma ficha
    :param nome: Nome a ser computado
    :param gols: quantidade de gols
    :return: nome, e gols do jogador
    """
    return f"O jogador {nome} fez {gols} gol(s) no campeonato."


#programação principal
print(Ficha(str(input("Nome do Jogador: ")), str(input("Número de Gols: "))))

#fim
# if c.isnumeric:
#     int(c)
