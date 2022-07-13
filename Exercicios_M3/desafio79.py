#Al:Usuário digita vários valores, cadastrar esses em uma lista. se o número existir na lista não será adicionado.
# exibir os valores em ordem decrescente
#autor: Lucas Borguezam
#data:

#Import

#Inicio
valores = []

while True:
    val = int(input("Digite um número: "))
    if val not in valores:
        valores.append(val)
    else:
        print("Este numero já foi armazenado.")
    cond = ' '
    while cond not in "sn":
        cond = str(input("Deseja continuar? [S/N]: ").lower().strip()[0])
    if cond == 'n':
        break
print("*-"*20)
valores.sort()
print(f"Você digitou os valores {valores}")
#fim
