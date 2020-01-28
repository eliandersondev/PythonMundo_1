'''
Desafio 013
Faça um algoritmo que leia o salário de um funcionário
e mostre seu novo salário com 15% de aumento.
'''

salario = float(input('Qual é o salário do Funcionário? R$'))
print('\nUm funcionário que ganhava R${:.2f}, com 15% de aumento \n'
      'passa a raceber R${:.2f}'.format(salario,salario*1.15))