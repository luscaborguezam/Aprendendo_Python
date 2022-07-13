#Al:Programa que receba uma frase no teclado e mostre
# Quantas vezes aparece a letra 'A'
# Posição que a parece a 1°vez
# em que posição aparece da ultima vez
#autor: Lucas Borguezam
#data:

#Import

#Inicio
frase = str(input("Digite a frase que você gosta: ")).strip().upper()

print("A letra 'A' apareceu {} vezes na frase".format(frase.count("A")))
print("1° posição de 'A' é {}".format(frase.find("A") + 1))
print("Ultina posição de 'A' é {}".format(frase.rfind("A") + 1))
#fim