#Al:Leia nome, anor de nascimento, carteira de trabalho, idade.
# Se CTPS !=0, cadastrar ano de contratação e o salário. Calcule:
# alem da idade, quantos anos a pessoa vai se aposentar
#autor: Lucas Borguezam
#data:

#Import
from datetime import datetime
#Inicio
aposentadoria = dict()
aposentadoria['nome'] = str(input("Nome: "))
aposentadoria['idade'] = int(datetime.now().year - int(input("Data de nascimento: ")))
aposentadoria['cpts'] = int(input("Carteira de Trabalho (0 caso não tenha): "))
if aposentadoria['cpts'] != 0:
    aposentadoria['contratação'] = int(input("Ano de contratação: "))
    aposentadoria['salário'] = float(input("Salário: R$"))
    aposentadoria['aposentadoria'] = aposentadoria['idade'] + (((aposentadoria['contratação'] + 35) - datetime.now().year))
print(f"{'Dados'}:-^45")
for k, v in aposentadoria.items():
    print(f"    {k.upper()} tem o valor {v}")

#fim
