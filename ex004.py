'''
Desafio 004
Faça um programa que leia algo pelo teclado e
mosttre na tela o seu tipo primitivo
e todas as informações possiveis sobre ela.
'''

vlr1 = input('Digite algo:')
print('O tipo primitivo dessa variavel é',type(vlr1))
print('É um número? ',vlr1.isnumeric())
print('Só tem espaços? ',vlr1.isspace())
print('É alfabético? ',vlr1.isalpha())
print('É alfanumérico? ',vlr1.isalnum())
