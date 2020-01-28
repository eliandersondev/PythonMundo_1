'''
Desafio 006
Crie um algoritmo que leia um número e mostre o seu
dobro, triplo e raiz quadrada
'''

import math

n1 = int(input('Digite um número:'))
dobro = n1 * 2
triplo = n1 * 3
raiz = math.sqrt(n1)

print('O dobro de {} é: {}'.format(n1,dobro))
print('O triplo de {} é: {}'.format(n1,triplo))
print('A raiz de {} é: {}'.format(n1,raiz))
