#Al: leia idade e sexo de n pessoas
#autor: Lucas Borguezam
#data:

#Import
maior18 = h = m20 = 0
#Inicio
while True:
    print(f"{'-'* 20}Cadastre uma pessoa {'-'*20}")
    ida = int(input("Qual sua idade? "))
    sex=""
    while sex not in "MF":
        sex = str(input("qual seu sexo? [M/F]").strip().upper()[0])
    if sex in "M":
           h += 1
    if ida > 18:
        maior18 += 1
        if sex in "F" and ida > 20:
            m20 += 1
    print('-'*40)
    condicao = ""
    while condicao not in "SN":
        condicao = str(input("Deseja continuar?[S/N] ").upper()).strip()[0]
        if condicao in "N":
            break
print(f"Maiores de 18 anos: {maior18}")
print(f"Homens cadastrados: {h}")
print(f"Mulheres com mais de 20 anos: {m20}")
#fim
