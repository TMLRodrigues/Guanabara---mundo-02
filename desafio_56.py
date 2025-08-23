"""
Desenvolva um programa que leia o NOME, IDADE e SEXO de QUATRO PESSOAS, no final do programa mostre:
- Média da idade do grupo
- Qual o homem mais velho
- Quantas mulheres tem menos de 20 anos
"""
med_idade=0
menor = 0
mais_velho = 0

for c in range (1,5):
   nome = str(input(f'Informe o nome da pessoa {c}º: '))
   idade = int(input(f'Informe a idade da pessoa {c}º: '))
   sexo = str(input(f'Informe o SEXO, utilize F = feminino e M = masculino, da pessoa {c}º: ')).upper()
   print('-'*40)
      #Media de idade do grupo
   med_idade = med_idade+idade
   idad=(med_idade/c)
   
   if sexo == 'F' and idade<=19:
        menor = menor +1
        print(menor)
   if sexo == 'M':
      if idade > mais_velho:
        mais_velho = idade
        print(mais_velho)
        
       
print(f'''
      A média da idade do grupo é: {idad} anos;
      O Homem mais velho é: {mais_velho} pessoa do sexo masculino;
      Mulheres abaixo de 20 anos: {menor} pessoas do sexo feminino.''')