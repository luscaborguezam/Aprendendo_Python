#Al: Programa que calcule o valor do almento do salário, superior a 1250 10%, inferior é 15%
#autor: Lucas Borguezam
#data:

#Import

#Inicio
sal = float(input("Informe seu salário para saber o aumento R$"))
aumento = sal*0.10if sal>1250.00 else sal*0.15

print("O aumento é de R${:.2f} do salário R${:.2f}\ntotal{:.2f}".format(aumento, sal, aumento+sal))
#fim
