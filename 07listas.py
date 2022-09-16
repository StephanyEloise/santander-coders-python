# 7. Estrutura de Listas // Array

# Antes

nota1 = 7.9
nota1 = 9.7
nota1 = 8.2

# Com lista

notas = [7.9, 9.7, 8.2]

# Criando Listas

lista = []
lista = list()
lista = [27, 'Midna', 3.1459, False]
lista_de_listas = [10, [1, 2, 3]]

# Indexação e Slices (fatiamento)

lista = [7, 'Eloise', 3.1415, True]

print(lista[0])  # 7
print(lista[1])  # Eloise
print(lista[2])  # 3.1415
print(lista[3])  # True

print(lista[-1])  # último, -2 penúltimo, etc

# Slice

lista = [10, 50, 30, 40, 25, 60, 5]

print(lista[0:3])  # [10, 50, 30]
print(lista[3:6])  # [40, 25, 60]
print(lista[3:6])  # [40, 25, 60, 5]
print(lista[2:6:2])  # 2 em 2 [30, 25]

# Interações com FOR

# 1. Utilizando os próprios elementos da lista

for elemento in lista:
    print(elemento)

# 2. Utilizando os índices

print('Comprimento da lista', len(lista))

for i in range(len(lista)):  # len = 7
    print(lista[i])


# Métodos de Listas

lista = [1, 3, 12, 8, 2]

# append - Add Final

print('Antes do append: ', lista)

lista.append(3)

print('Depois do append: ', lista)  # add 3 no fim

# insert - Add Escolhe a posição

lista.insert(2, 10)  # Add 10 no ind 2

print('Depois do insert: ', lista)

# extend - Pega os elementos e joga no fim

lista2 = [1, 2, 3]

lista.extend(lista2)

print('Depois do extend: ', lista)

# pop - Remove

lista.pop()  # Último

print('Lista após o pop: ', lista)

lista.pop(0)  # Primeiro

print('Lista após o pop: ', lista)

# remove - Escolhe o elemento para remover
# remove o primeiro que encontra

lista.remove(3)

print('Depois do remove: ', lista)

# count - Contar quantos elementos na lista

print('Quantidade de 2 na lista: ', lista.count(2))

# index

print('Índice do elemento 12: ', lista.index(12))

# sort - Organiza de forma crescente

lista.sort()  # sort(reverse=True) // revertido

print(lista)

# Funções para listas

# len

print(len(lista))  # 7 elementos

# sum

print(sum(lista))  # 38 total

# max

print('Maior elemento da lista: ', max(lista))

# min

print('Menor elemento da lista: ', min(lista))
