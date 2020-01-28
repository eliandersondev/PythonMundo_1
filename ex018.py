'''
Desafio 018
Faça um prograna que leia um ânguli qualquer e
mostre na tela o valor do seno, cosseno e tangente desse ângulo.
'''

from math import sin, cos, tan, radians

angulo = float(input('Digite o ângulo que você deseja:'))
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))
print('O ângulo de {:.1f} tem o SENO de {:.2f}'.format(angulo,seno))
print('O ãngulo de {:.1f} tem o COSSENO de {:.2f}'.format(angulo,cosseno))
print('O ângulo de {:.1f} tem a TANGENTE de {:.2f}'.format(angulo,tangente))
