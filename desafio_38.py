"""
Escreva um programa que leia DOIS NÚMEROS INTEIROS e compare-os:
- O primeiro valor é maior
- o segundo valor é maior
- Não existe valor maior, os dois são iguais
"""

valor1 = int(input('Informe um valor: '))
valor2 = int(input('Informe outro valor: '))

if valor1>valor2:
    print(f'O primeiro valor {valor1} é maior!' )
elif valor1<valor2:
    print(f'O segundo valor {valor2} é maior!')
else:
    print(f'Os primeiro valor {valor1} e o segundo valor {valor2}, são iguais!')