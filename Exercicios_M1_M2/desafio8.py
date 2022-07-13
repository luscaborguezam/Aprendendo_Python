#Al: leia um valor em metros, exibir a conversão em centimetros e milimetros
#autor: Lucas Borguezam
#data:08032022

#variáveis
m = 0.0
c = 0.0
mm = 0.0
#Inicio
m = float(input('Digite uma distância em metros: '))
c = m*100
mm = c*10

print('A distancia {}m, em centimetros é: {:.0f}cm, em milimetors é: {:.0f}mm.'.format(m, c, mm))

# ou
print('A distancia {}m, em centimetros é: {:.0f}cm, em milimetors é: {:.0f}mm.'.format(m, m*100, m*1000))


#Fim.