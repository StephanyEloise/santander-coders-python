from math import sqrt

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

mora_perto = input('Mora perto da vítima? ').lower() == 'sim'
trabalhou_com = input('Já trabalhou com a vítima? ').lower() == 'sim'
telefonou_para = input('Telefonou para a vítima? ').lower() == 'sim'
esteve_no_local = input('Esteve no local do crime? ').lower() == 'sim'
devia_para = input('Devia para a vítima? ').lower() == 'sim'

pontuacao_total = mora_perto + trabalhou_com + \
    telefonou_para + esteve_no_local + devia_para

if pontuacao_total == 5:
    print('Assassino! 😱')
elif pontuacao_total >= 3:
    print('Cúmplice 😨')
elif pontuacao_total == 2:
    print('Suspeito 🧐')
else:
    print('Liberado 🙌')


"""
Questão 6.
Faça uma função que recebe uma lista de números e retorna a soma dos elementos dessa lista.
"""


def somar_elementos(lista):
    soma = 0
    for elemento in lista:
        soma += elemento

    return soma


lista_de_exemplo = [4, 6, 7, 5, 3]
resultado = somar_elementos(lista_de_exemplo)

print('Soma dos elementos da lista =', resultado)


"""

Questão 7.
Faça um programa que leia as coordenadas de 2 (dois) pontos em um plano cartesiano 2D: a
coordenada x do primeiro ponto (x_1), a coordenada y do primeiro ponto (y_1), a coordenada x do
segundo ponto (x_2) e a coordenada y do segundo ponto (y_2). Em seguida, calcule a distância
euclidiana entre os pontos, utilizando a equação abaixo:
𝑑 = (𝑥2 − 𝑥1)² + (𝑦2 − 𝑦1)²

"""

x1 = float(input('Coordenada x do primeiro ponto: '))
y1 = float(input('Coordenada y do primeiro ponto: '))
x2 = float(input('Coordenada x do segundo ponto: '))
y2 = float(input('Coordenada y do segundo ponto: '))

distancia = sqrt((x2 - x1)**2 + (y2 - y1)**2)

print('Distância entre os pontos =', distancia)

"""

Questão 8.
Calcule a soma de mil termos dos inversos dos fatoriais: 1/(1!) + 1/(2!) + 1/(3!) + 1/(4!) + ...
Dica: Use três variáveis:
● um contador;
● uma variável para soma;
● e uma variável para os termos.
Lembre-se de que 4! = 4 * *3 ** 2 * *1, que também é igual a 4 ** 3

"""

contador = 1
soma = 0
termo = 1

while contador <= 1000:
    termo = termo / contador
    soma += termo
    contador += 1

print(soma)

"""

Questão 9.
Crie (manualmente ou sorteando os números) uma lista de 10 números e
imprima:
1. uma lista com os 4 primeiros números;
2. uma lista com os 5 últimos números;
3. uma lista contendo apenas os elementos das posições pares;
4. uma lista contendo apenas os elementos das posições ímpares;
5. a lista inversa da lista sorteada (isto é, uma lista que começa com
o último elemento da lista sorteada e termina com o primeiro);
6. uma lista inversa dos 5 primeiros números;
7. uma lista inversa dos 5 últimos números.

"""

lista = [5, 3, 9, 0, 1, 2, 6, 4, 7, 8]

print('Lista inicial:', lista, '\n')

print('Quatro primeiros elementos: ', lista[:4])
print('Cinco últimos elementos: ', lista[-5:])
print('Elementos nas posições pares: ', lista[::2])
print('Elementos nas posições ímpares: ', lista[1::2])

"""

Questão 10.
Na música, uma nota tem um tom (sua frequência, resultando em quão grave ou agudo é o
som) e uma duração (por quanto tempo a nota soa). Neste problema, estamos interessados
apenas na duração das notas.
Marcos está dando os primeiros passos para ser um compositor de jingles. Ele está tendo alguns
problemas, mas ao menos ele está criando melodias agradáveis e ritmos atrativos. Um jingle é
dividido em uma sequência de compassos, e um compasso é formado de uma série de notas.
A duração de uma nota é indicada pela sua forma. Neste problema, iremos utilizar letras
maiúsculas para indicar a duração de uma nota

A duração de um compasso é a soma da duração de suas notas. Nos jingles de Marcos, cada
compasso tem a mesma duração. Como Marcos é apenas um iniciante, seu famoso professor
Johann Sebastian III o ensinou que a duração de um compasso deve ser sempre 1.

Por exemplo, Marcos escreveu uma composição contendo cinco compassos, dentre os quais
quatro possuem a duração correta e um está errado.

Marcos gosta de computadores assim como de música. Ele quer que você escreva um programa
que determine, para cada uma de suas composições, quantos compassos possuem a duração
correta e quais são os compassos com duração incorreta.

"""

duracao_da_nota = {
    'W': 1,
    'H': 1/2,
    'Q': 1/4,
    'E': 1/8,
    'S': 1/16,
    'T': 1/32,
    'X': 1/64
}

composicao = '/HH/QQQQ/XXXTXTEQH/W/HW/'

# O método .strip() elimina o caracter que você colocar entre os parênteses, caso ele esteja no início ou no final da string
# O método .split() divide a string no caractere especificado entre os parênteses, gerando uma lista como resultado
compassos = composicao.strip('/').split('/')

qtd_corretos = 0
incorretos = []

for compasso in compassos:
    duracao_compasso = 0
    for nota in compasso:
        duracao_compasso += duracao_da_nota[nota]

    if duracao_compasso == 1:
        qtd_corretos += 1
    else:
        incorretos.append(compasso)

print('Qtd. de Corretos:', qtd_corretos)
if len(incorretos) > 0:
    print('Incorretos:', incorretos)
