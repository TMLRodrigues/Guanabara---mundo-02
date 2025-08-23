"""
Desenvolva um programa que leia SEIS NÚMEROS INTEIROS e mostre a soma apenas daqueles que forem PARES,
se o valor digitado por ÍMPAR, desconsider-o
"""
par = 0
print('Informe seis números inteiros: ')
for c in range (1,7):
    numero = int(input(f'Informe o {c}° número: '))
    if numero %2 == 0:
        par=par+numero
    print(f'Os resultado da soma dos números pares é: {par}')


    