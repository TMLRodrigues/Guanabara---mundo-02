"""
Desenvolva um programa que leia o PRIMEIRO TERMO e a RAZÃO de uma P.A.
No final, mostre os 10 primeiros termos dessa progressão.
an = a1(n-1)*r
a1 = primeiro termo
r = razão
n posição do termo
"""


progr_arit=0
prim_term = int(input('Informe o primeiro termo: '))
razao = int(input('Informe agora a razão: '))

# an = prim_term(n-1)*razão - apenas um anotação matemática
progr_arit = prim_term
print(prim_term)
for c in range(0,9):
    #progr_arit = prim_term + razao
    progr_arit = progr_arit + razao
    print(progr_arit)
