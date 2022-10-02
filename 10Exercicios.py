# Desafio // Exercício Santander Coders

"""

Questão 1.
Faça um programa que peça ao usuário um número e imprima todos os
números de um até o número que o usuário informar.

Exemplo:
Se o usuário informar o número 5, seu programa deverá imprimir: 1 2 3 4
5.

"""

from math import pi
numero = int(input('Digite um número: '))

for i in range(numero):
    print(i + 1, end=' ')

"""

Questão 2.
Crie um programa que leia um valor qualquer e apresente uma mensagem dizendo em qual
dos seguintes intervalos ([0,25], (25,50], (50,75], (75,100]) este valor se encontra. Caso o valor não
esteja em nenhum destes intervalos, deverá ser impressa a mensagem “Fora de intervalo”. Veja
alguns exemplo abaixo:
💡 Entrada: 25.01 | Saída: (25,50]
Entrada: 25.00 | Saída: [0,25]
Entrada: 100.00 | Saída: (75,100]
Entrada: -25.02 | Saída: Fora de intervalo
📌 Lembrando que o [ ou ] representa que o valor está contido no intervalo, enquanto o ( ou
) representa que o valor associado não está contido no intervalo. Em outras palavras, (75, 10

"""

if numero < 0 or numero > 100:
    print('Fora de intervalo')
elif numero <= 25:
    print('[0, 25]')
elif numero <= 50:
    print('(25, 50]')
elif numero <= 75:
    print('(50,75]')
else:
    print('(75,100]')

"""

Questão 3.
Crie uma função que recebe o valor do raio de um círculo como parâmetro e retorna o valor da
área desse círculo. Lembrando que a área de círculo é dada pela equação: A = ℼ r^2.
💡 Dica: Para utilizar um valor mais preciso do pi (ℼ), você pode importar a biblioteca math, e
utilizar o math.pi, como ilustrado no código abaixo:
import math
print(math.pi)

"""


def circulo(raio):
    return pi * raio ** 2


raio = 10
area = circulo(10)

print(area)

"""

Questão 4.
Faça um programa que peça 2 números inteiros e um número real,
calcule e mostre:
a) o produto entre o dobro do primeiro e a metade do segundo.
b) a soma entre o triplo do primeiro e o terceiro.
c) o terceiro elevado ao cubo.

"""
primeiro = int(input('Informe um número inteiro: '))
segundo = int(input('Informe outro número inteiro: '))
terceiro = int(input('Informe um número real: '))

# a
print('\nLETRA (a)')
dobro_do_primeiro = primeiro * 2
metade_do_segundo = segundo / 2
print('(2 x N1) * (N2 / 2) =', dobro_do_primeiro * metade_do_segundo)

# b
print('\nLETRA (b)')
triplo_do_primeiro = primeiro * 3
print('(3 x N1) + N3 =', triplo_do_primeiro + terceiro)

# c
print('\nLETRA (c)')
print('N3^3 =', terceiro ** 3)

"""

Questão 5.
Vamos fazer um programa para verificar quem é o assassino de um
crime. Para descobrir o assassino, a polícia faz um pequeno questionário
com 5 perguntas onde a resposta só pode ser sim ou não:
1. Mora perto da vítima?
2. Já trabalhou com a vítima?
3. Telefonou para a vítima?
4. Esteve no local do crime?
5. Devia para a vítima?

Cada resposta sim dá um ponto para o suspeito. A polícia considera que os suspeitos com 5
pontos são os assassinos, com 4 a 3 pontos são cúmplices e 2 pontos são apenas suspeitos,
necessitando de outras investigações. Valores abaixo de 2 são liberados.
No seu programa, você deve fazer essas perguntas e, de acordo com as respostas do usuário,
você vai informar como a polícia o considera.


"""
