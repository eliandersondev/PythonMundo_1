'''
Desafio 031
Desenvolva um programa que pergunte a distância de uma viagem em Km.
Calcule o preço da passagem, cobrando R$ 0,50 por km para viagens
de até 200km e R$ 0,45 para viagens mais longas.
'''


viagem = int(input('Qual é a distância da sua viagem: em Km '))
if viagem <= 200:
    passagem = viagem * 0.50
else:
    passagem = viagem * 0.45

print('O preço da sua passagem é R$ {}'.format(passagem))