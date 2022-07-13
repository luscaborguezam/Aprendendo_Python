#Al: Leia o ano de nascimento, e indique a classificação do atleta.
#autor: Lucas Borguezam
#data:

#Import
from datetime import date
#Inicio
ano = date.today().year
nasc = int(input("Ano de nascimento: "))
idade = ano - nasc
if idade <= 9:
    print("\033[1;36mMIRIM")
elif idade < 15:
    print("\033[1;34mINFANTIL")
elif idade < 20:
    print("\033[1;33mJUNIOR")
elif idade <21:
    print("\033[1;32mSÊNIOR")
else:
    print("\033[1;31mMASTER")

#fim
