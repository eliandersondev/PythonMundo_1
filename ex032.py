'''
Dessafio 032
Faça um programa que leia um ano qualquer e mostre
se ele é bissexto.
'''

ano = int(input('Digite um ano qualquer: '))
bissexto = False
if (ano % 4 ) == 0 and (ano % 100) != 0:
    bissexto = True
elif (ano % 400) == 0:
    bissexto = True
else:
    bissexto = False

print('O ano {} é bissexto? {}'.format(ano,bissexto))
