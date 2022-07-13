#ANSI - escape sequence '\'
#Código ansi para cores comssa com
#\033[style;text;back m
#\033[0;33;44m

#Codigos para:
#Estilo: 0(none), 1(negrito), 4(sublinhado) ,7(negative: inverte as configurações)
#Texto:  30(branco), 31(Vermelho), 32(verde), 33(amarelo), 34(azul), 35(roxo), 36(azul-cianu), 37(cinza)
#back(cor de fundo): 40(branco), 41(Vermelho), 42(verde), 43(amarelo), 44(azul), 45(roxo), 46(azul-cianu), 47(cinza)

# \033[0;30;41m
#
# \033[4;33;44m
#
# \033[1;35;43m
#
# \033[30;42m
#
# \033[m
#
# \033[7;30m

#print('\033[2;30;45mOlá Mundo\033[m')
a, b = [5,6]

print("os valores são \033[1;31;40m{} e {}\033[m".format(a, b))
nome ='Lusca'
#-----------//----------------
print("Olá muito prazer em te conhecer, {}{}{}!!!".format('\033[4;34m', nome, '\033[m'))
#-----------//----------------
cores = {"limpa":"\033[m",
         "azulciano":"\033[36m",
         "amarelo":"\033[33m",
         "pretoebranco":"\033[7;30m"}

print("Olá {}{}{}".format(cores["azulciano"], nome, cores["limpa"]))
#metodo colorize
