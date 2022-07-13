#Al: Função que retorna se a pessoa tem voto, OPCIONAL, OBRIGATÓRIO ou NEGADO
#de acordo com a data denascimento
#autor: Lucas Borguezam
#data:


#Import


#Inicio


def Voto(nasc = 0):
    from datetime import datetime
    ano = datetime.now().year
    idade = ano - nasc
    if idade < 16:
        return f"Com {idade} anos: Voto NEGADO"
    elif idade < 18 or idade > 65:
        return f"Com {idade} anos: Voto OPCIONAL"
    else:
        return f"com {idade} anos: Voto OBRIGATÓRIO"


anoNasc = int(input("Ano de nascimento: "))
print(Voto(anoNasc))

#fim
