#Variáveis Compostas
# Variáveis que armazena mais de um valor
#Tuplas ()
#listas []
#Dicionários {}

##### TUPLAS #####
# """As Tuplas são imutáveis"""
# não da para atribuir valores a tupla a não ser em sua declaração.
lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim') # Funciona sem parenteses

print(lanche)
print(lanche[:2])

for comida in lanche:
    print(f'Eu vou comer {comida}')
print('Comi muito!!\n\n')
print("--"*10)

for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')
print("Comi de mais.\n\n")
print("--"*10)

for posicao, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição: {posicao}')
print("To barrigudo!!")
print("--"*10)

print(sorted(lanche)) # sorted é ordenar ordem alfabética
print(lanche)
print("--"*10);

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b # a ordem dos fatores interferem no resultado
print(f"""  
            a = {a}
            b = {b}
            c = a + b
            c = {c}
""")

print(c.count(5)) #Quantas vezes aparece o numero 5
print(c.index(2)) #Mostra o index do número 2 armazenado na tupla
print(c.index(5, 1)) #Index do número 5 armazenado, verificação começa apartir index 1

pessoa = ("Lusca", 21, "M", 1.83)
del(pessoa) # Deleta a Tupla na memória