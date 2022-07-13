#Al: Simule um caixa eletronico
#autor: Lucas Borguezam
#data:

#Import

#Inicio
print(f"{'=='*15}")
print('{:^30}'.format("Banco"))
print(f"{'=='*15}")
valor = float(input("Valor para saque: R$"))
total = valor
cedula = 50
totalcedula = 0
while True:
    if total >= cedula:
        total -= cedula
        totalcedula += 1
    else:
        print(f"Total de {totalcedula} cédulas de R${cedula}")
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        totalcedula
        if total == 0:
            break
print("=="*30)
print('Volte sempre ao Banco!')
#fim
