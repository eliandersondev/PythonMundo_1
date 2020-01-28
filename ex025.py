'''
Desafio 025
Crie um programa que leia o nome de uma pessoas
e diga se ela tem 'SILVA' no nome.
'''

nome = str(input('Qual é o seu nome completo?')).strip()
print('Seu nome tem Silva? {}'.format(nome.upper().find('SILVA')!=-1))
print('Seu nome tem Silva? {}'.format('SILVA' in nome.upper()))