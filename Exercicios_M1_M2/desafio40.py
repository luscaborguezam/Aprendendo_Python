#Al: leia duas notas e calcule a média, mostrando abaixo(<5.0), média(5.0 e 6.9), aprovado (>7.0)
#autor: Lucas Borguezam
#data:

#Import

#Inicio
n1= float(input("Nota 1: "))
n2= float(input("nota 2 :"))
media= (n1+n2)/2

if media<5.0:
    print("\033[1;31mREPROVADO")
elif 5.0 <= media < 7: #media>=5.0 and media<=6.9
    print("\033[1;33mRECUPERAÇÂO")
else:
    print("\033[1;32mAPROVADO")

#fim
