
# Dictionary Comprehension e Set Comprehension 

-conteúdo
Quando vale pena usar Set Comprehension
Onde é aplicavél usar Dictionary Comprenhesion
## Dictionary Comprehension é jeito rapido de criar dioncarios assim como criar uma compreessão de lista 
# exemplo 1 mapeado e filtrando 
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

## Isso seria mais util  se vc precisar mapear de uma tupla pro exemplo.
```python
tupla_produtos = [('nome', 'caneta azul'), ('preco', 1.6), ('categoria', 'Escritorio')]

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


## Set comprehesion 
**Alerta** : Um set **Não** têm valores repetidos e **Não** têm ordem

```python
# Set Comprehesion remover duplicadas.

s1 = {
    i 
    for i in [1, 1, 2, 2, 3, 3]
}
print(s1)

```