'''
Desafio 030
Crie um programa que leia um número inteiro
e mostre na tela se ele é par ou ímpar
'''


num = int(input('Digite um número inteiro:'))
if (num % 2) == 1:
    print('Esse número é Ímpar.')
else:
    print('Esse número é Par.')