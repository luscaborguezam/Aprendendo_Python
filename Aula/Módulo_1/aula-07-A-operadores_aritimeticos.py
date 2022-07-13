##### Operadores Binários (precisam de dois operandos)
#Em Python igualdade é ==
# '+'  - Adição
# 5+2==6
# '-'  - Subtração
# 5-2==3
# '*'  - Multiplicação
# 5*2==10
# '/'  - Divisão
# 5/2==2.5
# '**' - Potência
# 5**2==25
# #ou pow(base,expoente)
#
# '//' - Divisão inteira (divide sem utilizar virgula)
# 5//2==2
# '%'  - Módulo (Resto da divisão)
#5%2==1
#25**(1/2) - raiz quadrada de 25
#125**(1,3) - raiz cubica de 125

#---------------------------------------------

#Ordem de Procedência
#1 ()
#2 **
#3  *, /, //, %
#4 + e -

# Em phyton podemos multiplicar texto
#'oi'*5 resulta em 'oioioioioi'

#-------------------------------
# Através do Format podemos utilizar alinhamento, desta forma
nome = input('Qial seu nome? ')
print('Prazer em te conhecer {:+^20}!'.format(nome))# com o '>' alinho para o final
                                                    # '^' Centraliza
                                                    # '20' é o numero de caracteres que a variavel vai ocupar
                                                    #ao colocar algo depois dos ':' ele completa os caracteres vazios

