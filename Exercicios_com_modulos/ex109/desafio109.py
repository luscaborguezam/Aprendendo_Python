#Al:Melhorando o ex:108 colocando um parametro opcional do retorno formatado
#autor: Lucas Borguezam
#data:

#Import
import moeda

#Inicio

p = float(input("Digite o preço: R$"))
print(f"A metade de {moeda.Moeda(p)} é {moeda.Metade(p, True)}.\n"
      f"O dobro de {moeda.Moeda(p)} é {moeda.Dobro(p, True)}.\n"
      f"Aumento de 10%, temos {moeda.Aumentar(p, 10, True)}.\n"
      f"Reduzindo 13%, temos {moeda.Diminuir(p, 13, True)}.")
#fim
