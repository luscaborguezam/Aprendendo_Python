#Al:Leia um preço e através de funções:
# aumentar o preço;
# diminuir preço;
# dobar o preço;
# dividir o preço.
#autor: Lucas Borguezam
#data:

#Import
import moeda

#Inicio

p = float(input("Digite o preço: R$"))
print(f"A metade de {p} é {moeda.Metade(p)}.\n"
      f"O dobro de {p} é {moeda.Dobro(p)}.\n"
      f"Aumento de 10%, temos {moeda.Aumentar(p, 10)}.\n"
      f"Reduzindo 13%, temos {moeda.Diminuir(p, 13)}.")


#fim
