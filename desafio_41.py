"""
A Confederação Nacional de Natação precisa de um programa que leia o
ANO DE NASCIMENTO de um atleta e mostre sua categoria de acordo com a idade:
- Até 9 anos: MIRIM
- Até 14 anos: INFANTIL
- Até 19 anos: JUNIOR
- Até 20 anos: SÊNIOR
- Acima: MASTER

"""

nome=input('Informe o nome do atleta: ')
idade = int(input('Informe a idade do atleta: '))

if idade <= 9:
    print(f'A categoria do atleta {nome} é MIRIM!')
elif idade > 9 and idade <= 14:
    print(f'A categoria do atleta {nome} é INFANTIL!')
elif idade > 14 and idade <= 19:
    print(f'A categoria do atleta {nome} é JUNIOR!')
elif idade == 20: # Como nesta condição cabe apenas um valor foi utilizado o operador ' == '
    print(f'A categoria do atleta {nome} é SÊNIOR!')
else:
    print(f'A categoria do atleta {nome} é MASTER!')