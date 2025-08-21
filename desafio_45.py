"""
Crie um programa que faça o computador jogar Jokenpô com você.
"""
import random
print('''Para jogar Jokenpô, escollha uma das opções:
      - 1 - Papel
      - 2 - Pedra
      - 3 - Tesoura
      ''')
usuario = int(input('Informe uma das opções: '))
if usuario != 1 and usuario !=2 and usuario!=3:
    print('Opção inválida para este jogo')
computador = random.randint(1,3)

if computador == 1:
    if usuario == 1:
        print ('Você jogou PAPEL e o computador jogou PAPEL - DEU EMPATE')
    elif usuario == 2:
        print('Você jogou PEDRA e o computador jogou PAPEL - VOCÊ PERDEU.')
    elif usuario == 3:
        print ('Você jogou TESOURA e o computador jogou PAPEL - VOCÊ GANHOU.')
if computador == 2:
    if usuario == 1:
        print ('Você jogou PAPEL e o computador jogou PEDRA - VOCÊ GANHOU')
    elif usuario == 2:
        print('Você jogou PEDRA e o computador jogou PEDRA - DEU EMPATE.')
    elif usuario == 3:
        print ('Você jogou TESOURA e o computador jogou PEDRA - VOCÊ PERDEU.')
if computador == 3:
    if usuario == 1:
        print ('Você jogou PAPEL e o computador jogou TESOURA - VOCÊ PERDEU')
    elif usuario == 2:
        print('Você jogou PEDRA e o computador jogou TESOURA - VOCÊ GANHOU.')
    elif usuario == 3:
        print('Você jogou TESOURA e o computador jogou TESOURA - DEU EMPATE.')
