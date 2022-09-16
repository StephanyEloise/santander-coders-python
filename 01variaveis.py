# 1. Variáveis

"""

1. int: números inteiros: 0, 5, -1, 1000
2. float: números reais: 1.0, -2.7, 3.14
3. str: cadeias de caracteres (string)
5. bool: valores lógicos (booleanos): True ou False

"""

idade = 27
altura = 1.66
nome = 'Stephany Eloise'
estudando = True  # case sensitive

print(type(idade))  # <class 'int'>
print(type(altura))  # <class 'float'>
print(type(nome))  # <class 'str'>
print(type(estudando))  # <class 'bool'>

# Obtendo dados do usuário e salvando em var
# Imprimindo variáveis + Mais sobre a função print

linguagem = input(
    'Qual é a linguagem de programação que você está estudando? ')

print('A linguagem que você está estudando é', linguagem)
