"""
Elabore um programa que calcule o valor a ser pago em um produto, considerando seu PREÇO NORMAL e CONDIÇÃO DE PAGAMENTO:
- Á VISTA dinheiro ou cheque: 10%;
- Á VISTA no cartão: 5%;
- 2X NO CARTÃO: preço normal;
- 3X NO CARTÃO: 20% de juros.
"""

produto=float(input('Informe o valor do produto: R$'))
print('''Escolha uma das formar de pagamento:
      - 1 - Á vista no cheque ou dinheiro - 10% de desconto;
      - 2 - Á vista no cartão - 5% de desconto;
      - 3 - 2x no cartão - preço normal;
      - 4 - 3x no cartão - acrécimo de 20% de juros
      ''')
form_de_pag = int(input('Informe a opção de pagamento: '))

if form_de_pag == 1:
    print(f'O valor da compra deu R$ {produto} e com desconto sairá R$ {produto*0.9}.')
elif form_de_pag == 2:
    print(f'O valor da compra deu R$ {produto} e com desconto sairá R$ {produto*0.95}.')
elif form_de_pag == 3:
    print(f'O valor da compra deu R$ {produto} e esta forma de pagamento não possui desconto.')
elif form_de_pag == 4:
    print(f'O valor da compra deu R$ {produto} e nesta forma de pagamento haverá um acréscimo de 20%, totalizando R$ {produto*1.2}')
else:
    print('Forma de pagamento inválida.')