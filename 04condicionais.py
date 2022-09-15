# 4. Estruturas Condicionais

idade = 20

if idade >= 18:
    print('Você é maior de idade.')
else:
    print('Você é menor de idade')

"""
Imagine que você queira imprimir "Aprovado(a), caso o estudante tenha média superior ou igual a 7, e "Reprovado", caso a média seja inferior a 7. 

"""

nota = float(input('Informe a média do estudante: '))

if nota >= 7:
    print('Aprovado(a)!')
elif nota >= 5:
    print('Recuperação')
else:
    print('Reprovado.')


media = 10
presenca = 100

if media >= 7 and presenca >= 70:
    print('Aprovado!')
else:
    print('Reprovado')

# else if = elif | && and
