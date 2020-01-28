'''
Desafio 029
Escreve um programa que leia a velocidade de um carro.
Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.
A muta vai custar R$ 7,00 por cada km acima do limite.
'''

vel = int(input('Digite a velocidade do carro:'))
if vel > 80:
    multa = (vel-80)*7
    print('Você foi multado por excesso de velocidade!')
    print('A multa vai custar R$ {:.2f}'.format(multa))
else:
    print('Você está dentro do limite de velocidade.')
print('Dirija com prudência.')