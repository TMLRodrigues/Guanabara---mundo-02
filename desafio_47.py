"""Crie um programa que mostre na tela todos os números pares que estão em um intervalo de 1e 50 """

print('=-'*22)
print('Mostrando todos os números pares de 1 a 50')
print('=-'*22)

for c in range (1,51):
    if c %2 == 0:
        print(c)
print('FIM')