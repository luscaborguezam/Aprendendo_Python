#Al:Leia nome e média do aluno guardand a situação em um dicionário, no final mostre o conteudo da estrutura na tela
#autor: Lucas Borguezam
#data:

#Import

#Inicio
ficha = dict()
ficha['Nome'] = str(input("Nome: "))
ficha['Média'] = float(input(f"Média de {ficha['Nome']}: "))
if ficha['Média'] < 6:
    ficha['Situação'] = str("Reprovado")
else:
    ficha['Situação'] = str("Aprovado")

for k, v in ficha.items():
    print(f"{k} é igual a {v}")
#fim
