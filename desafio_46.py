"""for c in range (1,6):
    print('Oi')
print('=-'*10)
print('Fim')
print('-='*10)"""

"""Faça um programa que mostre na tela a contagem regressiav para o estouro dos fogos de artifícios, indo de 10 a 0, com uma pausa de 1 segundo entre eles"""

from time import sleep
print('= '*11)
print('Contagem regressiva!')
print('= '*11)
for c in range (10, 0, -1):
    print(c)
    sleep(1)
    
print('= = !!! FOGO !!! = =')