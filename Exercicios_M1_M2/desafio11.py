#Al: leia altura e largura e calcule a area, e o tanto de tinta utilizada para pintar
#autor: Lucas Borguezam
#data:08032022

#tinta a cada 1L == 2m²

#variáveis
l=0.0
h=0.0
a=0.0
t=0.0
#Inicio
l=float(input('Largura da parede: '))
h=float(input('Altura da parede: '))
a=l*h
t= a/2

print('Sua parede tem a dimensão de {:.2f}x{:.2f} área da parede é: {:.2f}m²,\n'
      'É necessário {:.2f}L de tinta para pinta-la'.format(l, h, a, t))

#Fim.