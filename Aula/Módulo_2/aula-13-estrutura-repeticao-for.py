# Laços, repetições ou iterações
# FOR ==> estrutura de repetição com variável de controle.
#Estrutura FOR (Para)
# for variavel in range(0, 6, 2): #range vai de 0 a 5
#     print(variavel)
# print("FIM")
#
# for variavel in range(6, 0, -1):
#     print(variavel)
# print("FIM")

i = int(input("Início: "))
f = int(input("Fim: "))
p = int(input("Passo: "))

for c in range(i, f+1, p): # fim recebe +1 para mostrar o ultimo número
    print(c)
print("Fim")

#somatório
s= 0

for v in range(0, 3):
    n = int(input(print("Digite um valor inteiro")))
    s += n
print('O somatório de todos os valores foi {}'.format(s))
