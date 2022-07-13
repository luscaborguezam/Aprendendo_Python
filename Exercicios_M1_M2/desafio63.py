#Al: LEia um numero n e mostre os n priemeiros elementos de uma sequencia de fibonacci
#autor: Lucas Borguezam
#data:

#Import

#Inicio
# 0 - 1 - 1 - 2 - 3 - 5 - 8
#t1 - t2 = t3
n = int(input("Quantos Termos você quer mostrar?"))
t1 = 0
t2 = 1
print('{} -> {}'.format(t1, t2), end='')
cont = 3 #ja foi mostrado 2 termos
while cont <= n:
    t3 = t1 + t2
    print(" -> {} -> ".format(t3), end='')
    t1 = t2
    t2 = t3
    cont += 1
print("Fim")
#fim
