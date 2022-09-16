# 6. Laços de Repetição "For"

for variavel in range(10):  # 0 a 9
    print(variavel)

for variavel in range(1, 6):  # 1 a 5
    print(variavel)

for variavel in range(1, 12, 3):  # 3 em 3
    print(variavel)

"""

nota1 = float(input('Informe sua nota 1: '))
nota2 = float(input('Informe sua nota 2: '))
nota3 = float(input('Informe sua nota 3: '))

"""

soma = 0

for i in range(1, 4):  # 1,2,3
    nota = float(input(f'Informe a sua nota {i}: '))

    soma = soma + nota

print(soma / 3)
