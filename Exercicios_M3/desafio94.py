#Al: leia nome, sexo, idade, de n pessoas, guardando o nome de cada pessoa em um dicionário
# , e cada dicionário em uma lista. Mostre:
# qtd de pessaos cadastradas.
# média de idade do grupo
# lista com todas as mulheres
# lista com pessoas com idade acima da média.
#autor: Lucas Borguezam
#data:

#Import

#Inicio
dados = dict()
pessoas = list()

while True:
    dados.clear()
    dados['nome'] = str(input("Nome: ")).strip().title()
    while True:
        dados['sexo'] = str(input("Sexo [M/F]: ")).strip().upper()[0]
        if dados['sexo'] in 'MF':
            break
        else:
            print("Erro!, porfavor digite apenas M ou F")
    dados['idade'] = int(input("idade: "))
    pessoas.append(dados.copy())
    while True:
        cond = str(input("Quer continuar? [S/N]:").lower().strip()[0])
    if cond in 'SN':
        if cond == 'n':
            break
    else:
        print("Escolha as opções 'S' ou 'N'")
somaidade = 0
for c in pessoas:
    somaidade += c['idade']
idaMedia = round(somaidade/len(pessoas))

print("-="*50)
print(f"- Foram cadastrado {len(pessoas)} pessoas.")
print(f"- Média entre as idades é: {idaMedia}")

print("- Mulheres cadastradas:")
for c in pessoas:
    if c['sexo'] == 'F':
        print(f" =>{c['nome']}")

print(f"- Pessoas com a idade Acima da média ({idaMedia}):")
for c in pessoas:
    if c['idade'] > idaMedia:
        print(f"    =>{c['nome']}")
#fim
