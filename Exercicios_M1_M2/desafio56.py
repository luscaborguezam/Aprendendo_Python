#Al: leia nome, idade e sexo de 4 pessoas, mostre média de idade do
# grupo, nome do homem mais velho, quantas mulheres de 20 anos
#autor: Lucas Borguezam
#data:1205

#Import

#Inicio
somaIdade = 0
idadeMulher = 0
maisVelho = 0
nomeVelho = ""
for pessoas in range(1, 4+1):
   print("---{}°Pessoa---".format(pessoas))
   nome = str(input("Digite seu nome: ")).strip()
   idade = int(input("Informe sua idade: "))
   sexo = str(input("Sexo[F/M]:")).strip()
   somaIdade += idade

   if sexo in "Mm":
       if(maisVelho == 0):
           maisVelho = idade
       if(maisVelho <= idade):
           nomeVelho = nome
   if sexo in "Ff":
       if(idade<20):
           idadeMulher += 1

print("Média da idade: {}".format(somaIdade/pessoas))
print("Homem mais velhor: {}".format(nomeVelho))
print("Mulheres menores de 20 anos: {}".format(idadeMulher))

#fim
