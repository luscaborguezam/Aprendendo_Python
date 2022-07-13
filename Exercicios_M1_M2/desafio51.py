#Al: Progressão aritimética, ler o 1° termo e a razão de uma PA, mostrar os 10 primeiros termos dessa progressão
#autor: Lucas Borguezam
#data:

#Import

#Inicio
# print("=" * 12)
# print("10 TERMOS DE UMA PA")
# print("=" * 12)
# Ptermo = int(input(print("1° Termo: ")))
# razao = int (input(print("Razão: ")))
# termos = 0
# for c in range(0, 10):
#     termos = Ptermo+(c)*razao
#     print("{}° - Termo é {}".format(c+1, termos))

# correção
primeiro = int(input(print("1° Termo: ")))
razao = int (input(print("Razão: ")))
decimo = primeiro + (10 - 1) * razao

for c in range(primeiro, decimo + razao, razao):
    print("{}".format(c), end=">> ")
print("Acabou")
#fim
