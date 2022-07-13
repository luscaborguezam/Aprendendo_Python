#Pr: Programa que aprova empréstimos, recebe valor da casa, salário, periodo de tempo (em anos) que vai
# pagar a prestação, se o valor da prestação exceder 30% do salário será negada
#autor: Lucas Borguezam
#data:

#Import

#Inicio
imovel = float(input(print("Valor do imóvel: R$")))
salario = float(input(print("Salário do solicitante: R$")))
periodo = int(input(print("Periodo em anos do total de prestações: "))) #
prestacao = imovel/(periodo*12)
print("Para pagar um imóvel de R${:.2f} no periodo de {} anos".format(imovel, periodo))
print("A prestação será de {:.2f}".format(prestacao))

if (salario*0.3) < prestacao:
    print("\033[31mEmpréstimo \033[1mNEGADO\033[m")
else:
    print("\033[;32mEmpréstimo \033[1mCONCEDIDO\033[m")


#fim
