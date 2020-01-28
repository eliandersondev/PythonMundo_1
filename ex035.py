'''
Desafio 035
Desenlvolva um programa que leia o comprimenro de três retas e diga ao usuário
se elas podem ou não formar um triângulo.
'''
print('Vamos testar se as retas formam um triângulo.')
r1 = int(input('Digite um comprimento de reta: '))
r2 = int(input('Digite um comprimento de reta: '))
r3 = int(input('Digite um comprimento de reta: '))

if r1 > (r2 + r3):
    print('Não forma um triângulo')
elif r2 > (r1 + r3):
    print('Não forma um triângulo')
elif r3 > (r1 + r2):
    print('Não forma um triângulo')
else:
    print('Você formou um triângulo')