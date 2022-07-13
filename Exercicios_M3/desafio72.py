#Al: Programa que tenha armazenado por estenso o nome dos númeors de 0 a 20, ao usuário inserir um número nesse range
# mostrar o número por extenso
#autor: Lucas Borguezam
#data:

#Import

#Inicio
numeros = ("zero","um", "dois", "três", "Quatro", "cinco", "sies", "sete", "oito", "nove", "dez", "onze", "doze", "treze",
           "quatorze", "quinze", "dezesseis", "dezessete", "dezoito", "dezenove", "vinte")

while True:
    while True:
        n = int(input("Digite um número entre 0 e 20: ").strip())
        if 0 <= n <= 20:
            break
        else:
            print("Tente Novamente. ", end='')
    print(f"Você digitou o número {numeros[n]}")
    condicao = " "
    while condicao not in "SN":
        condicao = str(input("Deseja continuar?[S/N] ")).strip().upper()[0]
    if condicao in "N":
        break

#fim
