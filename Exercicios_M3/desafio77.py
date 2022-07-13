#Al: Tupla, com várias palavras. mostrar as vogais de cada palavra
#autor: Lucas Borguezam
#data:

#Import

#Inicio
palavras = ("aprendiz", 'cliente', "professor", "salario", "colchao", "ponto", "virgula", "concatenar")

for item in palavras:
    print(f'\nNa palavra {item.upper()} temos: ', end='')
    for letra in item:
        if letra in 'aeiou':
            print(letra, end=' ')
#fim
