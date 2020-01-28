'''
Desafio 033
Faça um programa que leia três números e mostre
qual é o maior e qual é o menor.
'''

lista = []
lista.append(int(input('Digite um número inteiro: ')))
lista.append(int(input('Digite um número inteiro: ')))
lista.append(int(input('Digite um número inteiro: ')))

lista.sort()
print('\33[1;33;44mO menor valor é {} e o maior valor é {}.\33[m'.format(lista[0],lista[2]))