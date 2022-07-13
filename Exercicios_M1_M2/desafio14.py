#Al: leia um valor em c° e transforme em Ffahrenheit
#autor: Lucas Borguezam
#data:15032022

#variáveis
c=0.0
f=0.0
#Inicio
c = float(input("Digite a temperatuda c°"))
f = ((c*9)/5)+32

print("A conversão de {:.1f}C° para fahrenheit é: {:.1f}°f".format(c, f))
#Fim.