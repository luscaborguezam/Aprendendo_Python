#Al: Simule um caixa eletronico
#autor: Lucas Borguezam
#data:

#Import

#Inicio
print(f"{'=='*10}Bem vindo!!{'=='*10}")
valor = float(input("Valor para saque: R$"))
n50 = n20 = n10 = n1 = 0
resto = 0.0
while True:
    if 0 > valor > 1:
        resto = valor
    if valor < 1:
        break
    else:
        if valor >= 50:
            valor -= 50
            n50 += 1
        elif valor >= 20:
            valor -= 20
            n20 += 1
        elif valor >= 10:
            valor -= 10
            n10 += 1
        elif valor >= 1:
            valor -= 1
            n1 += 1
print(f"{n50} Cédulas de R$50.00\n"
      f"{n20} Cédulas de R$20.00\n"
      f"{n10} Cédulas de R$10.00\n"
      f"{n1} Cédulas de R$01.00\n"
      f"Saldo restante: R${resto:.2f}")
#fim
