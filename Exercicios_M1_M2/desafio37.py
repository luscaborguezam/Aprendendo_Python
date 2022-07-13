#Al: converta um nunmero inteiro em base binário ou octagonal ou hexadecimal.
#autor: Lucas Borguezam
#data:

#Import

#Inicio
n = int(input(print("Escolha um número: ")))
print("Escolha base para conversão de {}\n"
      "[1] - BINÁRIO\n"
      "[2] - OCTAGONAL\n"
      "[3] - HEXADECIMAL".format(n))
base = int(input((print(">> "))))
if base == 1:
    print("{} convertido para binário é: {}".format(n, bin(n)[2:]))
elif base == 2:
    print("{} convertido em OCTAGONAL é: {}".format(n, oct(n)[2:]))
elif base == 3:
    print("{} converdito em HEXADECIMAL é: {}".format(n, hex(n)[2:]))
else:
    print("Opção iválida tente novamente.")

#fim
