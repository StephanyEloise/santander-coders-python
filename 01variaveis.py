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

# 2. Operações Matemáticas (Ariméticas)

"""

- Soma: + 
- Subtração: - 
- Multiplicação: * 
- Divisão: / 
- Divisão inteira: // 
- Resto da divisão: % 
- Potência: ** 

"""

numero1 = 10
numero2 = 20

print(numero1 + numero2)  # 30
print(numero1 - numero2)  # -10
print(numero1 * numero2)  # 200
print(numero1 / numero2)  # 0.5
print(numero1 // numero2)  # 0
print(20 % 3)  # 2
print(2 ** 3)  # 8

# Operadores Booleanos

idade1 = 10
idade2 = 15
altura1 = 1.77
altura2 = 1.65
altura3 = altura2

print(idade1 > idade)          # false
print(idade1 <= idade)         # true
print('Python' == 'python')    # false
print('banana' != 'abacaxi')   # true
print(altura1 >= altura2)      # true
print(altura2 > altura3)       # false
