"""
Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
O programa vai perguntar o 
VALOR DA CASA;
SALÁRIO DO COMPRADOR;
QUANTOS ANOS DESEJA PAGAR.
Calcule o valor da prestação mensal, sabendo que ela não pode ultrapassar 30% do salário informado ou o empréstimo será negado.
"""

print('Empréstimo para a compra de uma casa')
val_res = float(input('Informe o valor total da residência que deseja adquirir: '))
salario = float(input('Informe seu salário líquido mensal: '))
tempo = int(input('Informe em quantos anos deseja pagar este imóvel'))
prestacao = val_res/(tempo*12)
trinta = salario*0.3

#print( trinta, prestacao)

if prestacao<trinta:
    print(f'Parabéns seu emtréstimo foi aprovado: \nParcela: R${prestacao}\nTempo: {tempo} ano(s)')
else:
    print(f'Infelizmente seu emprestimo não foi aprovado,\npois o valor da prestação ultrapassar 30% da sua renda mensal.\nPrestação:R${prestacao}\nValor máximo da parcela: R${trinta}')
    

