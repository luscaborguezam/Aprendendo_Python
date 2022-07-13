#Al: mostre numeros pares entre 1 e 50 usando for
#autor: Lucas Borguezam
#data:

#Import

#Inicio
for c in range(1, 50+1):
    print('.', end=' ') #indica quantas vezes o laço foi executado
    if c%2 == 0:
        print(c)
# ou

for n in range(2, 51, 2):
    print(".") #indica quantas vezes o laço foi executado
    print(n, end=' ')
#fim
