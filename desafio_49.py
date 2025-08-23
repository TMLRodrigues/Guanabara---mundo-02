'''
Refaça o DESAFIO 09,
    FAÇA UM PROGRAMA QUE LEIA UM NÚMERO INTEIRO QUALQUER E MOSTRE NA TELA SUA TABUADA
mostrando a tabuada de um número que o usuário escolhor, só que com o laço FOR'''

tabuada = int(input('Informe a tabuada que deseja visualizar: '))
for c in range(0,11):
    print('{} x {} = {}'.format(tabuada, c, (c*tabuada)))