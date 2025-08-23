"""
Crie um programa que leia o ano de nascimento de SETE PESSOAS, no final mostre quantas pessoas ainda não
atingiram a maioridade e quantas já são menores    
"""
from datetime import date
print('Programa para mostrar quantas pessoas são MAIORES E MENORES de idade!')

maior_idade = 0
menor_idade = 0
ano_nascimento = int
ano_atual = date.today().year
for c in range(1,8):
    ano_nascimento = int(input(f'Informe o {c} ano de nascimento: '))
    if (ano_atual - ano_nascimento) <18:
        menor_idade = menor_idade +1
    else:
        maior_idade = maior_idade +1

print(f'Dos valores informados \n{menor_idade} são menores de idade \n{maior_idade} são maiores de idade.')
    
    
    