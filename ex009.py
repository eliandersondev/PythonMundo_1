'''
Desafio 009
Faça um programa que leia um número inteiro e mostre
na tela a sua tabuada.
'''

n = int(input('Digite um número para ver a tabuada:'))

print('- ' * 7)
for i in range(1,11,1):
    print('{} x {:2} = {:3}'.format(n,i,(n*i)))
print('- ' * 7)