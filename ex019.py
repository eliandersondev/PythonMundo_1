'''
Desafio 019
Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome escolhido.
'''

from random import randint

lista = []

lista.append(input('Primeiro aluno:'))
lista.append(input('Segundo aluno:'))
lista.append(input('Terceiro aluno:'))
lista.append(input('Quarto aluno:'))

escolhido = randint(0,3)
print('O aluno escolhido foi {}.'.format(lista[escolhido]))