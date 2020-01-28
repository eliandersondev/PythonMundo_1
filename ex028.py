'''
Desafio 028
Escreva um prograna que faça o computador pensar em um número inteiro
entre 0 e 5 e peça para o usuario tentar descobrir qual foi o número
escolhido pelo computador.
O programa deverá escrever na tela se o usuário venceu ou perdeu.
'''

from random import randint

n1 = randint(0,5)
n2 = int(input('Escolha um número inteiro entre 0 e 5:'))
if n1 == n2:
    print('Você venceu! PARABÉNS!')
else:
    print('Você perdeu! hahahaha...!')