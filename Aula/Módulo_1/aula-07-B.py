n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
s = n1+n2
m = n1*n2
d = n1/n2
di= n1//n2
e = n1**n2
print('A Soma é: {}, o produto é:{} e a divisão é: {:.3f}'.format(s, m, d))
# Para limitar as casas decimais mostradas usa depois dos ':' '.nf' n= numero de casas, f= flutuantes
# para juntar as linhas no final do print utilizar ", end='  '" e para quebra de linha "\=n"
print('A divisão inteira é: {}, e a potência é: {}'.format(di, e))
