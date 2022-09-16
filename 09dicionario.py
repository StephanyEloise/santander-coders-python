# Dicionário

# Criando dicionários

dicionario = {}
dicionario = dict()

dicionario = {'nome': 'Midna', 'idade': 27, 'altura': 1.66}

print(dicionario)
print(dicionario['idade'])

# Adicionando elementos em um dicionário

dicionario['programador(a)'] = True

print(dicionario)

dicionario['nome'] = 'Stephany Eloise'

print(dicionario)

# Iterando sobre um dicionário

for chave in dicionario:
    print(chave, dicionario[chave])
    # percorre a chave e o valor

# Testando a existência de uma chave

print('peso' in dicionario)  # false
print('altura' in dicionario)  # true
