#Al: adicione varios númros em uma lista, e mostre:
# A)Quantos n° foram digitados
# b)Lista ordenada decrescente
# C)Se o valor 5 foi digitado e está  ou não na lista
#autor: Lucas Borguezam
#data:

#Import

#Inicio
lista= []
while True:
    n = int(input("Digite um valor: "))
    lista.append(n)
    cond = ' '
    while cond not in 'sn':
        cond = str(input("Deseja Continuar? [S/N]: ").strip().lower()[0])
    if cond == 'n':
        break
lista.sort(reverse=True)
print(f"Foram digitaedos {len(lista)} números\n"
      f"Lista:{lista}")
print(f"Valor 5 na posição {lista.index(5)}" if 5 in lista else "5 não foi digitado")
#fim
