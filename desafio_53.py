"""
Crie um programa que leia uma frase qualquer e diga se ela é um PALINDROMO, desconsidereando os espaços.
len len(frase)
split frase.split()
frasesemespacos = frase.replace(' ','')
MAS ERA PARA TER CRIANDO COM UM 'FOR', SÓ NO FIM QUE EU ME LEMBREI, VOU DEIXAR ASSIM MESMO
"""

#Transformei a frase informada em maiúculo, sem espaços no início, fim e no meio da frase
frase=(input('Informe um frase: ')).upper().strip().replace(' ','')
#print(frase) foi apenas um teste para ver se estava imprimindo corretamente

#variável para guardar o palindromo, já invertendo seu comprimento
palindro= frase[len(frase)+1::-1]

#condição, verificação da frase se é igual a frase invertida
if frase == palindro:
    print(f'A fase informada {frase} invertida é {palindro}, logo esta frase é um palindromo.')
else:
    print('sua frase NÃO é um PALINDROMO')

#print(f'A frase informada foi:{frase.upper()} e ela invertidada é:{palindro}')