'''
Desafio 022
'''

nome = input('Digite seu nome completo:').strip()
espacos = nome.count(' ')
separa = nome.split()

print('\nAnalisando seu nome...\n')

print('Seu nome em maiúsculas é {}'.format(nome.upper()))
print('Seu nome em minúsculas é {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome) - espacos))
print('Seu primeiro nome é {} e ele tem {} letras'.format(separa[0],len(separa[0])))