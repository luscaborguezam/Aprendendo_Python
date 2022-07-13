#Al: Mostre a quantidade de Km percorridos por carro alugado e a quantidade de dias pelos quais ele foi
# alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por km rodado
#autor: Lucas Borguezam
#data:16032022

#variáveis
km=0.0
d=0
total=0.0
#Inicio
km = float(input('Qual a quantidade de quilômetros percorrido km'))
d = int(input('Quantos dias de aluguel?'))

total = (km*0.15)+(d*60)
print('O valor a pagar pelos {:.1f}km rodados e os {} dias de uso é: {:.2f}'.format(km, d, total))
#Fim.