# inteiro int
n1 = int(input('Dgite um numero: '))
n2 = int(input('Digite um valor: '))
#saber o tipo primitivo de uma variavel com o comando type
#print(type(n2))
#Menssagem de saida com metodo format
s = n1+n2
#print('A soma de ', n1 ,' e ', n2 ,'é: ', s)
# ou
print('aA soma entre {} e {} vale {}'.format(n1, n2, s))
# metodo isnumeric retorna se o valor da variável pode ser convertido para int (inteiro)

n = input('Digite um valor: ')
print('O valor inserido tem só numeros inteiro?')
print(n.isnumeric())

# metodo isalpha retorna se o valor da variável é alfabético pode ser convertido para str
print('O valor inserido só tem letras?')
print(n.isalpha())

# metodo isalnum retorna se o valor da variável pode ser convertido para alphanumerico
print('O valor inserido é alphanumerico?')
print(n.isalnum())

# metodo isupper retorna se o valor da variável tem somente letas maiusculas?(islower se está em minusculo)
print('O valor inserido contem apenas letras maisculas?')
print(n.isupper())

# isprinttavble(se pode ser impresso)
