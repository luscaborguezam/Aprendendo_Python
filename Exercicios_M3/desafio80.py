#Al: lista que recebe 5 valores, e colocar em ordem crescente sem o método sort
#autor: Lucas Borguezam
#data:

#Import

#Inicio
lista =[]
for c in range(0, 5):
    n = int(input(f"Digite o {c+1}° valor: "))
    # Se o valor for o 1° digita do ou maior que o ultimo será adicionado na posição sequencial
    if c == 0 or n > lista[-1]:
       lista.append(n)
       print("Adicionado ao final da lista...")
    else:
    #se não, vai verificar cada item na lista, e se o número digitado for menor ou igual a um dos itens
    # ele é adicionado na posição do item verificado
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f"Adicionado na posição {pos} da lista...")
                break
            pos+=1
print(f"Os valores inseridos em ordem são: {lista}")
#fim
