"""
Refaça o deseafio 35:
DESAFIO 35: DESENVOLVA UM PROGRAMA QUE LEIA O COMPRIMENTO DE TRÊS RETAS
            E DIGA AO USUÁRIO SE ELAS PODEM OU NÃO FORMAR UM TRIÂNGULO.
Acrescentando o recurso de mostrar que tipo de triângulo será formado:
EQUILÁTERO: todos os lados iguais;
ISÓCELES: dois lados iguais;
ESCALENO: todos os lados diferentes.
"""

reta1 = int(input('Informe um valo para a primeira reta: '))
reta2 = int(input('Informe um valor para a segunda reta: '))
reta3 = int(input('Informe um valor para uma terceira reta: '))

if reta1+reta2>reta3 and reta1+reta3>reta2 and reta2+reta3>reta1:
    #print('Os valores informados podem formar um triângulo.') - Esta é a linha do exercício 35, não achei necessário executá-lo.
    if reta1 == reta2 and reta1 == reta3 and reta2 == reta3:
        print('Estes valores formam um triângulo - EQUILÁTERO!')
    elif reta1 == reta2 or reta1 == reta3 or reta2 == reta3:
        print('Estes valores formam um triângulo - ISÓCELES!')
    else:
        print('Estes valores formam um triângulo - ESCALENO!')
else:
    print('Os valores informados NÃO podem formar um triângulo.')