'''
Desafio 015
Escreva um programa que pergunte a quantidade de km percorridos
por um carro e a quantidade de dias pelos quais ele foi alugado.
calcule o preço a pagar, sabendo que o carro custa R$60 por dia
e R$0,15 por km rodado.
'''

dias = int(input('Quantos dias alugados?'))
km = int(input('Quantos Km rodados?'))
total = (dias * 60) + (km * 0.15)

print('\nO total a pagar é de R${:.2f}'.format(total))