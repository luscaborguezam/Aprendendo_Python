#     #Tratar cadeia de caracters
#       '''
#       toda cadeia de caracter em python vem acompanhada com '' ou "" ou ''''''
#       Chamada de STRINGS
#       '''
# frase = 'Curso em Video Python'
#         '''
#         o computador não armazena em um local como um indice,
#         cada caracter ocupa 1 mini-espaço na memória armazenada. a frase acima tem 21 caracters (0 a 20 - Ranges)
#         '''
# #Algumas operações
# #Fatiamento de string
# frase[9]# resulta na letra "V"
# frase[9:13]# resulta uma mine cadeia do V:O porem não mostra o ultimo caracter resultando em: "Vide"
# frase[9:21]#V:n resultado "Video python" não existe o 21, mas o python não o considera
# frase[9:21:2]# o ultimo item '2' referencia o espaço de ranges que vai ser mostrados, resultado:
#              # VdoPto ou seja vai de 9 a 21 pulando em 2 em 2
# frase[:5] # antes do ':' é o iniico depois é o fim ou seja
#           # incio da frase até o 5 resultado "Curso"
# frase[15:]#quando não é definido o fim ou o inicio ao pithon ele considera o resto
#           #Resultado "Python" do 15 ao fim
# frase[9::3] #do 9 até o fim mostrando a cada 3 range
#             #Resultado "VePh"
#         '''
#         operações com cadeia de string
#         Análise
#         qual o tamanho dela?
#         qual letra ela começa ou termina?
#         qual a primeira palavra inteira?
#
#         '''CATEGORIAS DE FUNCIONALIDADES
# #análise
# len(frase) # len é de comprimento = 21 micro-espaço
# frase.count('o') # contar quantos 'o' existe na variavel. Lembrando que python diferencia O de o
#                  # resultado 3
# frase.count('0', 0, 13) #contar "o" no range de 0:13 resultado:1. no fatiamento o ultimo range definido é ignorado
#
# frase.find('deo')# find(encontrar). Diz em qual momento começou o 'deo' resultado:11
# frase.find('android')# quando coloca o valor de uma string que não existe na variável o find retorna '-1'
# 'Curso' in frase #Dentro da variavel frase existe essa string? Operador in retorna sim ou não
#
# #Transformação
# #Uma string com os seus micro elementos são imutaveis, a não ser que se use uma função de transformações de string e faça
# #uma atribuição
#
# frase.replace('python','androird');#subsiui python por android na strnge
# frase.upper() #Deixa tudo maiusculo
# frase.lower()#deixa tudo minusculo
# frase.capitalize()#Deixa apenas  a primeira letra maiuscula e o resto ninuscula
# frase.title()#Deixa a primeira letra de cada palavra maiuscula
# frase.strip()#Deleta todo espaço inutil da esquerda e direita.
# frase.rstrip()#remove somente os espaços da 'r'-rigth direita
# frase.lstrip()#remove somente os espaços da 'l'-left esquerda
#
# #Divisão
# frase.split() #uma divisão considereando os espaços dentro da string, gerando uma nova lista com as palavras sendo item
#               #separadas pelo caracter de split' ' -"espaço".
#               # ex:
#               """
#               frase= "Lucas Gabirel Borguezam"
#               frase.split()
#               frase= 1-"Lucas"
#                      2-"Gabriel"
#                      3-"Borguezam"
#               """
# #junção
# '-'.join(frase)#junta as palavras que eram indices tendo como separador o '-'.
#     # ex:
#         """
#         frase="Lucas-Gabriel-Borguezam
#         """