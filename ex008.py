'''
Desafio 008
Escreva um programa que leia um valor em metros
e o exiba convertido em centimetros e milimetros.
'''

distancia = float(input('Digite uma distância em metros:'))
print('A medida de {}m corresponde a:'.format(distancia))
print('{}km'.format(distancia/1000))
print('{}hm'.format(distancia/100))
print('{}dam'.format(distancia/10))
print('{}m'.format(distancia))
print('{}dm'.format(distancia*10))
print('{}cm'.format(distancia*100))
print('{}mm'.format(distancia*1000))