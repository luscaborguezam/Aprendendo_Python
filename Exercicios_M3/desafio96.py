#Al: Faça uma função area(), receba dois largura e comprimento de um terreno retangular e mostre a área.
#autor: Lucas Borguezam
#data:

#Import

#Inicio
def area(larg, compri):
    area = larg * compri
    print(f"A área de um terreno {larg}X{compri} é {area:.2f}m².")


#Programa principal
print(f"{'Calculando Área':-^30}")
a = float(input("Largura (m): "))
b = float(input("Comprimento (m): "))
area(larg=a, compri=b)

#fim
