# While
# Usado quando não sabemos o numero exato de repetições necessárias
# estrutura de repetição com teste lógico
i = 0
while i < 10:
    print(i)
    i = i + 1
print("FIM")

n = 1
while n != 0: # confição de parada
    n = int(input("Digite um valor:"))
print("Fim")

c = 'S'
while c == "S":
    n = int(input("Digite um valor"))
    c = str(input("Quer Continuar [S/N]? ")).upper()
print("fim")
