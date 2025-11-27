
# Dictionary Comprehension e Set Comprehension 

- 
- Aplicações reais continua ....


## Dictionary Comprehension 
### É uma forma **rapída, clara e concisa** de criar de diciónarios em uma uníca linha assim como list comprehension, com a diferença **pares chave e valor**

## Exemplo 1 - **Mapeado e Filtrando** 
```
produto = {
    'nome': 'caneta azul',
    'preco': 2.5,
    'categoria': 'Escritorio'
}

dc = {
    chave: valor 
    for chave, valor in produto.items()
}
print(dc)

```

## Exemplos 2 - A partir de **lista/tupla de pares**.
```python
tupla_produtos = [
    ('nome', 'caneta azul'),
    ('preco', 1.6),
    ('categoria', 'Escritorio')
]

dc = {
    chave : valor 
    for chave, valor in tupla_produtos
}
print(dc)

```

### Erros inesperados.

```python
# Dictionary Comprehension e Set Comprehension 
produto = {
    'nome': 'caneta azul',
    'preco': 2.5,
    'categoria': 'Escritorio'
}

dc = {
    chave: valor 
    for chave, valor in produto.items()
}
#pesquisar o porque ao desempacotar somente chaves aparecem 
print(*dc)
#Saida 
nome preco categoria

```


## Set comprehension 

- Set comprehension é usado para criar `set` **conjutos sem repetição**.
- É usado para **remover duplicadas** 
- **Não matém ordem**,
- **Não aceita valores duplicados**.

```python
s1 = {
    i 
    for i in [1, 1, 2, 2, 3, 3]
}
print(s1)
# Saída
{1, 2, 3, 4}

```
