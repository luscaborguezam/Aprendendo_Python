#Al: Leia uma frase e diga se é um polindromo
#autor: Lucas Borguezam
#data:

#Import

#Inicio
frase = str(input(print("Diga uma palavra ou frase que deseja: "))).strip().upper()# elimina espaços extremos. ex: LUCAS LOKO
palavra = frase.split() # Quebra a frase em lista. ex: ['LUCAS', 'LOKO']
junto = ''.join(palavra) # une os elementos. ex:LUCASLOKO
# da para eliminaro for usnado:
# inverso = junto[::-1] # macete de fatiamento
inverso = ''

for letra in range(len(junto) - 1, -1, -1): # len(junto) - 1 o começo da contagem de uma string começa do 0, len 20 (0 ao 19)
    inverso += junto[letra]
print("O inverso de {} e {}".format(junto, inverso))

if inverso == junto:
    print("Temos um palíndromo".format(frase))
else:
    print("A frase digitada não é um palíndromo")


#fim
