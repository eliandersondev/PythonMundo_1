'''
Desafio 012
Faça um algoritmo que leia o preço de um produto
e mostre seu novo preço com 5% de desconto.
'''

produto = float(input('Qual é o preço do produto? R$'))
desconto = produto * 0.95
print('O produto que custava R${:.2f},\nna promoção com desconto '
      'de 5%\nvai custar R${:.2f}'.format(produto,desconto))