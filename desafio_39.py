"""
Faça um programa que leio o ANO DE NASCMENTO de uma pessoa e informe:
- AINDA VAI SE ALISTAR
- É A HORA DE SE ALISTAR
- JÁ PASSOU DA HORA DE SE ALISTAR
seu programa deverá mostrar quanto tempo falta ou se passou do prazo de alistamento obrigatório.    
"""

ano_nasc = int(input('Informe o seu ano de nascimento: '))
idade = 2025 - ano_nasc
alista = 18 - idade

print(alista, idade)

if idade < 18:
    print(f'Sua idade é {idade} anos e falta(m) {alista} ano(s) para seu alistamento obrigatório.')
elif idade == 18:
    print(f'Sua idade é {idade} anos e este é seu ano de alistamento obrigatório, PARABÉNS!\nCOMPAREÇA A UMA JUNTA MILITAR MAIS PRÓXIMA!')
elif idade > 18:
    print(f'Sua idade é {idade} anos e já passou {alista} ano(s) do seu alistamento obrigatório.')
    