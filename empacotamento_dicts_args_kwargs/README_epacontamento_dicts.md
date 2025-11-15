# Empacotamento e Desempacotamento com `dicts args kwargs`
Resumo baseado na aula 83

## Conteúdo
- Para que servem os operadores `* **`.
- Entendedo Packing (Empacotamento).
- Entendedo Unpacking (Desempacotamento).
- 📎 Exemplos desempacotamento empacotamento sem funções.
- O que são argumentos posicionais (`args`).
- O que são argumentos nomeados (`kwargs`).


## O que seria o asterisco `*`
 Ele serve para`Upacking e Packing` valores
 
 Quando você usa `*` em um **parametro de função** ele empacota varios argumentos em uma tupla!

Exemplo empacotamento ´Pancking´
```python
def soma (* numeros)
   return sum(numeros) 

total = soma(1, 2, 3)
print(total) 
```
Saida:
```
# resultado 6
```
 `*` para `Unpacking` **desempacotar argumentos**

Exemplo (Unpacking)
```python
 numeros =(1, 2, 3, 4)
 print(* numeros) 
```
Saida 
```python
1 2 3 4 
```
------------------------------------------------------------------------
## O uso do asterisco duplo `**`
`Packing` Empacotamento.
Quando usado `**` em **argumentos nomeados** os chamados (kwargs) são empacotados em `dict`.

Exemplo
```python
 def mostar_dados(** dados)
    return dados

processamento =mostrar_dados(nome=janio, idade=20)
print(processamento) 
```
Saida
```python
 {"nome":"janio", "idade": 20}
```
desempacotando `Unpacking`.
```pyhton
dados_usuario = {"nome":"janio", "idade": 20}

def mostar_dados( dados)
    return dados

processamento = mostrar_dados(dados_usuario)
print(´**`processamento) 
```
Saida

```python
"nome":"janio", "idade": 20
```
------------------------------------------------------
## 📎 Exemplos desempacotamento empacotamento sem funções

# Empacotamento ´Packing` sem o uso asterisco
```python
a, b = 1, 2        # `Packing` normal
a, b = b, a        # troca usando `Packing` + 
print(a, b)
```

# Até string podem ser Unpacking
```python
letras = [janio]
print(*letras)
Saida
[j, a, n, i, o] 
```
# Juntando dicionarios 

```python
pessoa = { 
    "nome": "Aline",
    "sobrenome": "Souza",
}
(a1, a2 ), (b1, b2)= pessoa.items()
print(a1, a2, b1 , b2)

dados_pessoas = {
    "altura": 1.60,
    "idade": 28
}



pessoa_completa = {}
# desempacotando em terceiro dicionário
pessoa_completa= {**pessoa, **dados_pessoas} 

print(pessoa_completa)
```

#### Fixe o que aprendemos sobre  `Unpacking` "Desempacotamento", `Packing` "Empacotamento"


## Podemos usa-los em:

. Nas chamada função

. Nas criação de listas, dicionarios.

. Nas atribuição de valores

. em loops



----------------------------------------

## Argumentos posicionais `args`
**Argumetos posicionais** `args` são valores passados **sem nome**,e que cuja a  **ordem importam** e que são passados `*args` e todos esses valores são passados como uma tupla.
```python
def somar (* numeros) # args
    return sum (numeros)

total = somar(1, 3, 5, 6,)
```
Saida
```python
 print(total) 
```


# Argumentos Nomeados (`**kwargs`) e o Uso do Duplo Asterisco

Argumentos nomeados são aqueles em que a **ordem não importa**, pois cada valor já vem acompanhado de seu nome.  
Exemplo: `texto(a=10, b=20, c=11)`  

O uso do duplo asterisco `**` permite **capturar ou desempacotar argumentos nomeados** em forma de dicionário.

| Situação                         | O que faz                                   | Exemplo                                   | Resultado                              |
|----------------------------------|--------------------------------------------|-------------------------------------------|----------------------------------------|
| Dentro da definição da função     | Captura argumentos nomeados em um dicionário | `def f(**kwargs): print(kwargs)`          | `f(a=1, b=2)` → `{'a': 1, 'b': 2}`   |
| Na chamada da função              | Desempacota um dicionário em argumentos nomeados | `dados = {'a': 1, 'b': 2}` <br> `f(**dados)` | `a=1, b=2` passado para `f`           |