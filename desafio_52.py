"""
Faça um programa  que leia um número inteiro e diga se ele é ou não
um número PRIMO
"""
from time import sleep
total = 0
print('-'*60)
print('Programa para verificar se o número informado é primo ou não')
print('-'*60)
num = int(input('Informe um número: '))

for c in range (1, num+1):
    if num % c == 0:
        print('\033[31m', end='') #sistemas de cores peguei do vídeo
        total = total+1
    else:
        print('\033[33m', end='') #sistemas de cores peguei do vídeo
        
    print(c, end=' ')
print(f'\n\033[mO número informado é divisível {total} vezes, logo ...') #sistemas de cores peguei do vídeo
if total == 2:
    sleep(1)
    print('\033[32mEste número é PRIMO')
else:
    sleep (1)
    print('\033[36mEste número NÃO É PRIMO')

#Neste desafio eu recorri parcialmente ao VÍDEO RESOLUÇÃO para completar o desafio ...