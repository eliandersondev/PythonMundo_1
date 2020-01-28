'''
Desafio 011
Faça um programa que leia a largura e a altura
de uma parede em megtros.
Calcule a sua área e a quantidade de tinta
necessária paa pinta-la.
Sabendo que cada litro de tinta, pinta uma área de 2m2.
'''

largura = float(input('Largura da parede:'))
altura = float(input('Altura da parede:'))
area = largura * altura
litros = area / 2
print('Sua parede tem a dimensão de {:.2f}x{:.2f} /'
      'e sua área é de {:.2f}m2'.format(largura,altura,area))
print('Para pintar essa parede, você precisará /'
      'de {:.2f}l de tinta.'.format(litros))