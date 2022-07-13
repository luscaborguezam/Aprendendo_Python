#estrutura condicional dentro de uma outra estrutura condicional
nome = str(input("qual seu nome? "))
if nome.lower() == 'lucas' or nome.lower()=='gabriel':
    print("{}, Que nome bonito".format(nome.title()))
elif nome.lower() == 'borguezam':
    print("{}, Super DLÇÂO".format(nome.title()))
else:
    print("{}, Seu nome é ruim ".format(nome.title()))