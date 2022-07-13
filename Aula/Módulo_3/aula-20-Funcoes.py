#Funções
# Estão vinculados a palavra Rotina
# Ações que fazemos constantemente
# Acompanhadas com parentezes ex: func(), print(), len()
#Funções sem parâmetros -----------------------------------------------
print("#Funções sem parâmetros")
def Lin():
    return print('-'*40)


Lin()
print(f"{'Lucas':^40}")
Lin()
Lin()
print(f"{'Gabriel':^40}")
Lin()
Lin()
print(f"{'Borguezam':^40}")
Lin()

# Usando Parâmetros -----------------------------------------------
print('# Usando Parâmetros')

def mensagem(msg):
    print('-' * 30)
    print(msg)
    print('-' * 30)


mensagem(f'{"Lucas":^30}')
mensagem(f"{'Borguezam':^30}")
Lin()
print()

# Pratica
print("# Pratica")

def soma(a, b):
    print(f"A = {a} e B = {b}")
    s = a + b
    print(f"A soma de A + B = {s}") #ou return


print("Função soma()")
soma(2, 3)
soma(b=4, a=5)
Lin()
print()

#Empacotamento -----------------------------------------------
print('Empacotamento usando "*"')
print("Soma")
def somarDes(*valores):
    s=0
    for num in valores:
        s += num
    print(f"A soma dos valores {valores} é {num}")
somarDes(7, 3 ,1)
Lin()
def contador(*num): # '*' é o desempacotador, faz a variavel num receber todos os parâmentros como uma tupla
    tam = len(num)
    print(f"Recebi os valores {num}, ao todo são {tam} números")


contador(2, 1, 7)
contador(8, 0)
contador(9, 5, 3, 7)
Lin()
print()
#Dobrando valores de uma lista  -----------------------------------------------
print("Dobrando valores de uma lista")
def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


valores = [6, 3, 9, 1, 0, 2]
print(f"lista: {valores}")
dobra(valores)
print(valores)