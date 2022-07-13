x = input(print('Digite algo: '))
print('O tipo primitivo desse valor é ', type(x))

print('só tem espaço? ', x.isspace())
print('É número?', x.isnumeric())
print('É alfabético? ', x.isalpha())
print('É um alphanumérico? ', x.isalnum())
print('Está em maiusculo? ', x.isupper())
print('Está em minusculo', x.islower())
print('Está capitalizada(maiusculo e minusculo)? ', x.istitle())
print('Pode ser impressa?', x.isprintable())

# x é um objeto, e os atributos que terminam com () são métodos.
# no caso métodos do tipo string