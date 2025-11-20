# Dictionary Comprehension e Set Comprehension 
'''
produto = {
    'nome': 'caneta azul',
    'preco': 2.5,
    'categoria': 'Escritorio'
}

dc = {
    chave: valor.upper()
    if isinstance(valor, str) else valor
    for chave, valor
    in produto.items()
}
print(dc)

'''
tupla_produtos = [('nome', 'caneta azul'), ('preco', 1.6), ('categoria', 'Escritorio')]

dc = {
    chave : valor 
    for chave, valor in tupla_produtos
}
print(dc)



# Set Comprehesion remover duplicadas.

s1 = {
    i 
    for i in [4, 4, 1, 1, 2, 2, 3, 3]
}
print(s1)

