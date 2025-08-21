"""
Crie um programa que leia duas notas de um aluno e calcule sua média,
mostrando a mensagem no final, de acordo com a média atingida:
- Abaixo de 5,0 = reprovado
- Entre 5,0 e 6,9 = recuperação
- Acima de 7,0 = aprovado.
"""

print('=== PROGRAMA QUE MOSTRA A MÉDIA DO ALUNO ===')
nome=input('Digite o nome do aluno: ')
nota1=float(input('Informe a primeira nota: '))
nota2= float(input('Informe a segunda nota: '))
media=(nota1+nota2)/2

print(media)

if media < 5:
    print(f'O aluno {nome} infelizmente foi REPROVADO! =[')
elif media >= 5 and media <7:
    print(f'O aluno {nome} está de RECUPERAÇÃO! =|')
elif media >= 7:
    print(f'O aluno {nome} está APROVADO, PARABÉNS! =]')
