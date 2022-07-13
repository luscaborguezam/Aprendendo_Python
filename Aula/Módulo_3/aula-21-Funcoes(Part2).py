# Função interna para ajuda interativa help()
# no phyton Console digitar help()
# Mostra as caracteristicas dos comandos ou funções
# Para sair é usat exit
# ou ultilizar assim:
help(print)
# ou imprimir o __doc__ do comando
print("--"*10,
      "\nusando o: .__doc__ ")
print(input.__doc__) #mostra informações da funções
print("--"*10,
      "\nUsando o: help()")
help(input)

print("\n\n")
print("""# na função com parâmetros temos:
# *Parâmetros Reais: passados na chamada da função 
# *Parâmetros Formais: são aqueles que pertencem a função.\n""")
print("DOCSTRINGS")
print("São o manual deixado para entender a função,\n"
      "se localiza logo abaixo do comando def,\n"
      "usando aspas duplas 3x")
# Exemplo abixo

def contador(i, f, p):
    """
    -> Faz uma contagem e mostra na tela
    :param i: início da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno
    Função criada por Lucas.
    """
    con = i
    while con <= f:
        print(con, end='..')
        con += p
    print("FIM!")


help(contador)
print("--------------------------------------")
# --------------------------------------------------------------------------
#Parâmetros Opcionais
print("#Parâmetros Opcionais")
# ao adicionar =0 após o parâmetro indica que
# o parâmetro recebera o valor 0 caso não tenha informado algum valor para ele
def somar (a=0, b=0, c=0):
    """
    -->Faz soma de três valores e mostra o reesultado na tela
    :param a: primeiro valor
    :param b: segundo valor
    :param c: terceiro valor
    :return: sem retorno
    Função criada por Lucas.
    """
    s = a + b + c
    print(f"A soma vale {s}")

somar(3, 2, 5)
somar(8, 4)
somar()
print("--------------------------------------")
# -----------------------------------------------------------------------------
# Escoppo de variáveis
print("# Escoppo de variáveis\n"
      "# Escopo local, escopo global\n")
# Variáveis local e global


def teste(b):
    #variáveis locais
    a = 8
    b+=4
    c=2
    print(f"A dentro vale {a}")
    print(f"B dentro vale {b}")
    print(f"C dentro vale {c}")


#variáveis global
a = 5
teste(a)
print(f"A fora vale {a}")
print()
# assim como as bibliotecas importações globais ou locais


def teste2(b):
    global d
    d = 8
    print(f"B vale {b} aqui dentro")
    print(f"D vale {d} aqui dentro")


d = 5
teste2(d)
print(f"D vale {d} aqui fora")
print("--------------------------------------")
# ---------------------------------------------------------------------------------
#Retorno de Valores retunr
print("#Retorno de Valores: RETURN")


def somando(a=0, b=0, c=0):
    s = a + b + c
    return s


r1 = somando(3, 2, 5)
r2 = somando(2, 2)
r3 = somando(3)
print(f"O resultado das somas são {r1}, {r2}, {r3}")
print()
#-------------------------------------

def Par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False


num = int(input('Digite um número: '))
if Par(num):
    print("É par")
else:
    print("É impar")