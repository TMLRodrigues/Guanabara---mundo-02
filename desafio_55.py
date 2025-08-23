"""
Faça um programa que leia o peso de CINCO PESSOAS. No final mostre qual foi o MAIOR e o MENOR peso lido.
"""
peso = 0
peso_maior = 0
peso_menor = 100000000000 #um jeito 'porco de resolver'
print('Program para ler o MAIOR e o MENOR peso.')

for c in range(1,6):
    peso = int(input(f'Infome o {c}° peso (kg): '))
    if peso > peso_maior:
        peso_maior = peso
    elif peso < peso_menor:
        peso_menor = peso
print(f'Maior peso digitado foi: {peso_maior} kg')
print(f'Menor peso digitado foi: {peso_menor} kg')