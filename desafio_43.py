"""
Desenvolva uma lógica que leia o PESO e a ALTURA de uma pessoa, calcule o IMC
e mostre o status, de acordo com a tabela abaixo:
- 18,5: abaixo do peso
- 18,5 a 25: peso ideal
- 25 a 30: sobrepeso
- 30 a 40: obesidade
- Acima de 40: obesidade mórbida
"""

altura = float(input('Informe a sua altura em metros (M): '))
peso = float(input('Informe o seu peso em quilos (KG): '))
#IMC = peso/(altura x altura)

imc= float(peso/(altura*2))

if imc < 18.5:
    print(f'A medida deu {imc:.2f}, isto indica BAIXO PESO - CUIDADO!')
elif imc >= 18.5 and imc < 25:
    print(f'a medida deu {imc:.2f}, isto indica PESO IDEAL - PARABÉNS!')
elif imc >= 25 and imc < 30:
    print(f'a medida deu {imc:.2f}, isto indica SOBREPESO - CUIDADO!')
elif imc >=30 and imc<40:
    print(f'a medida deu {imc:.2f}, isto indica  OBESIDADE - CUIDADO')
else:
    print(f'A medida deu {imc:.2f}, isto indica OBSIDADE MÓRBIDA - CUIDADO!')