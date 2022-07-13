#Al: Programa que leia o ano de nascimento e informe se ainda vai; se é a hora; ou já passou da hora de se alistar
#autor: Lucas Borguezam
#data:

#Import
from datetime import date
#Inicio
import dateutil.utils
sexo = str(input("SEXO\n"
                 "(M)-masculino\n"
                 "(F)-feminino:\n"
                 ">> "))
if sexo == 'm' or sexo == 'M':
    nascimento = int(input("Ano de nascimento: "))
    ano = date.today().year


    idade = ano - nascimento
    if idade == 18:
        print("Está na hora de se alistar")
    elif idade > 18:
        saldo = idade - 18
        print("Seu alistamento foi em {} ano".format(ano - saldo))
        print("Está atrasado {} anos, seu desleixado, deixa 10 flexôes, e vai se alistar!!!".format(saldo))
    else:
        saldo = 18 - idade
        print("Falta {} anos para você se alistar".format(18 - idade))
        print("Seu alistamento será em {} ano".format(ano + (18 - idade)))
else:
    print("O serviço militar obrigatório é somente para homens")
#fim

