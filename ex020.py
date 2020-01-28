'''
Desafio 020
O professor quer sortear a ordem de aprensentaao de trabalhos dos alunos.
Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
'''

from random import shuffle

lista = []
lista.append(input('Primeiro aluno:'))
lista.append(input('Segundo aluno:'))
lista.append(input('Terceiro aluno:'))
lista.append(input('Quarto aluno:'))

shuffle(lista)
print('\nA ordem de apresentação será')
print(lista)