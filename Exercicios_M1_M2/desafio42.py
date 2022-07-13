#Pr: Refaser o exercicio desafio35 mostrando que tipo de triangulo pode ser formado, equilatero, isóceles, escaleno
#autor: Lucas Borguezam
#data:

#Import

#Inicio
print("--"*20)
print("Calculadora de existencia de Treiângulo")
print("--"*20)
a = int(input("Primeiro segmento: "))
b = int(input("Segundo segmento: "))
c = int(input("Terceiro segmento: "))
if (a+b)>c and (b+c)>a and (a+c)>b:
    print("É possível formar um triângulo")
    if (a == b and c != a) or (a == c and b != a ) or (c == b and a != c):
        print("Forma um triângulo ISOCELES")
    elif a == b == c:
        print("Forma um triângulo EQUILÁTERO")
    elif a != b and a != c and c != b:
        print("Forma um triângulo ESCALENO")
else:
    print("Impossível formar um triângulo.")


#fim
