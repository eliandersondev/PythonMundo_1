'''
Desafio 034
Escreva um programa que pergunte o salário de um funcionário e calcule
o valor do seu aumento.
Para salários superiores a R$ 1.250,00, calcule um aumento de 10%.
Para os inferiores ou iguais, o aumento é de 15%
'''

sal = float(input('Digite o seu salário: R$ '))
if sal > 1250:
    aumento = sal * 0.10
else:
    aumento = sal * 0.15

print('O aumento de salário foi de R$ {:.2f}, agora o seu salário é de R$ {:.2f}'.format(aumento,aumento+sal))