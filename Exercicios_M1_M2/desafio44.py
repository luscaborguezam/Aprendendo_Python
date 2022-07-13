#Al: Programa que calcule o preço da venda de um produto considerando a condição de pagamento: dinheiro 10% desconto
#até 2x no cartão sem desconto, 3x ou maior q 3x 20% de juros
#autor: Lucas Borguezam
#data:

#Import

#Inicio
preco = float(input(print("Informe o Preço do produto: R$")))
print("TIPO DE PAGAMENTO:\n[1]-a vista\n[2] - até 2x no cartão\n[3] - 3x ou mais no cartão\n[4] - a vista no cartão\n")
escolha = int(input(print(">> ")))
if escolha == 1:
    total = preco - (preco * 0.1)
elif escolha == 2:
    parcelas = int(input(print("1 ou 2 parcelas?")))
    total = preco
    print("Pagamento será em {}x de {:.2f}R$".format(parcelas, preco/parcelas))
elif escolha == 3:
    i = int(input(print("Informe quantas parcelas (OBS: o minimo é acima de 2 parcelas)")))
    parcelas = i
    if parcelas < 2:
        print("O minimo de parcela para esta opção é 3, faça novamente.")
    else:
        total = preco + (preco*0.2)
        print("Pagamento será em {}x de {:.2f}R$".format(parcelas, total/parcelas))
elif escolha == 4:
    total = preco - (preco * 0.05)
else:
    total=0
    print("Opção inválida de pagamento, tente novamente")
print("Sua compra de R${:.2f} vai custar R${:.2f} no final".format(preco, total))

#fim
