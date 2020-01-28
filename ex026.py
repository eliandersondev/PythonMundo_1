'''
Desafio 026
Faça uma programa que leia uma frase pelo teclado e mostre:
Quantas vezes aparece a letra 'A'.
Em que posição ela aparece a primeirea vez.
Em que posição ela aprece a última vez.
'''

frase = str(input('Digite uma frase:')).strip().upper()
num = frase.count('A')
n1 = frase.find('A')+1
n2 = frase.rfind('A')+1
print(num,n1,n2)