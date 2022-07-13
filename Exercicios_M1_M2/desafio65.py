#Al: receba n numeros, condição de parada 0, média nos numeros digitados e maior e menor valor
#autor: Lucas Borguezam
#data:

#Import

#Inicio
i = 1
acu =0
cont = 0
maior = 0
menor = 0
op = "S"
while op in "Ss":
        i = int(input("digite um valor:\n>>"))
        acu += i
        if cont == 1:
            maior = i
            menor = i
        elif maior <= i:
            maior = i
        elif menor >= i:
            menor = i
        op = input("Deseja Continuar? [S/N]")
        cond = 0
        while cond == 0:
            if op in 'SsNn':
                cond = 1
            else:
                print("Opção inválida")
                op = input("Deseja Continuar? [S/N]")
        cont += 1
print("Você digitou {} númeors e a média entre eles é: {}\nMaior valor: {}\nMenor valor: {}".format(cont, acu/cont, maior, menor))
#fim
