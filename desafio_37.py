"""
Escreva um programa que leia um número inteiro qualquer e peça para o usuario escolher qual será a BASE DE CONVERSÃO,
1 = BINÁRIO
2 = OCTAL
3 = HEXADECIMAL
"""

num = int(input('Informe um número inteiro: '))
print('''Veja as opções de conversão:
       - 1 - = Conversão para BINÁRIO;
       - 2 - = Conversão para Octal;
       - 3 - = Conversão para HEXADECIMAL.
      ''')
op=int(input('Digite sua opção: '))

if op == 1:
    print(f'O valor {num} convertido para BINÁRIO é:{bin(num)}')
elif op == 2:
    print(f'O valor {num} convertido para OCTAL é: {oct(num)}')
elif op == 3:
    print(f'O valor {num} convertido para HEXADECIMAL é: {hex(num)}')
else:
    print('opção inválida!')
    

