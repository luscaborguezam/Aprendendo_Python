#Al: Programa cim uma tupla com nomes de produtos e seus respectivos preços na sequência
#       Mostrar uma listagem de preços organizando os dados em forma tabular
#autor: Lucas Borguezam
#data:

#Import

#Inicio
produtos = ("Lápis", 1.735, "Borracha", 2, "Caderno", 15.9, "Estojo", 25, "Transferidor", 9.99, "Compasso", 4.2,
            "Mochila", 120.32, "Canetas", 22.3, "Livro", 34.9)
print("-="*20)
print(f"{'listagem de preço'.upper():^40}")
print("-="*20)
for p in range(0, len(produtos), 2):
    print(f"{produtos[p]:.<30}R${produtos[p+1]:.2f}")
print("-="*20)

# ou
print("_-"*20)
print(f"{'Correção'.upper():^40}")
print("_-"*20)
for pos in range(0, len(produtos)):
    if pos%2 == 0:
        print(f"{produtos[pos]:.<30}", end='')
    else:
        print(f"R${produtos[pos]:.2f}")
print("_-" * 20)
#fim
