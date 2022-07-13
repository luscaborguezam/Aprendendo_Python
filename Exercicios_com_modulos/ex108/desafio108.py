# al: Mesmo exercicio 107, com valores formatados
#autor: Lucas Borguezam
#data:

#Import
import moeda

#Inicio

p = float(input("Digite o preço: R$"))
print(f"A metade de {moeda.Moeda(p)} é {moeda.Moeda(moeda.Metade(p))}.\n"
      f"O dobro de {moeda.Moeda(p)} é {moeda.Moeda(moeda.Dobro(p))}.\n"
      f"Aumento de 10%, temos {moeda.Moeda(moeda.Aumentar(p, 10))}.\n"
      f"Reduzindo 13%, temos {moeda.Moeda(moeda.Diminuir(p, 13))}.")


#fim

