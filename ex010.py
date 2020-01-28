'''
Desafio 010
Crir um programa que leia quanto dinheiro uma
pessoa tem na carteira e mostre quantos dolares
ela pode comprar.
'''

real = float(input('Quanto dinheiro você tam na carteira: R$'))
cambio = 3.27
dolar = real/cambio

print('Com R${:.2f} você pode comprar US${:.2f}'.format(real,dolar))