"""Faça um programa que calcule a soma entre todos os númeors ímpares que são multiplo de três e que se encontram no intervalo de 1 até 500"""

soma = 0

print(' * * * '*9)
print('Soma dos números ÍMPARES multiplos de TRÊS entre 1 até 500')
print(' * * * '*9)

for c in range (1, 500):
    if c %3 == 0:
        if c %2 != 0:
            soma=soma+c
            print(c)
            #print (f'Soma ={soma}')
    
print (soma)
print('Fim')