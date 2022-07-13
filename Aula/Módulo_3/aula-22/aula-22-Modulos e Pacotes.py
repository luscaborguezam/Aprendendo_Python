#Modularização: ato de construir módulos
# década de 60, devido o tamanho grande do programa.
# Divide o programa em módulos
# Se torna mais legivel
# Aumenta a legibilidade
# Facilita a Manutenção
# para o python todos arquivo.py pode ser um módulo

from uteis import numeros #Funcionalidades estão no arquivo numeros.py
# usado para evitar ambiguidade em nome de funções
# em caso de ambiguidade de nome, o ultimo a ser importado sera reconhecido pelo python.

num = int(input("Digite um valor "))
fat = numeros.fatorial(num)
print(f"O fatorial de {num} é {fat}")
print(f"O triplo de {num} é {numeros.triplo(num)}")
print(f"O Dobro de {num} é {numeros.dobro(num)}")

# Vantagens
# Organização do código
# Facilita na manutenção
# Ocultação do código detalhado
# Reutilização em projetos

#Pacotes (Bibliotecas) Quando a modularização fica muito sobrecarregado
# Pacote, pasta de módulos separados por assuntos
# podendo importar apenas funções de um determinado assunto