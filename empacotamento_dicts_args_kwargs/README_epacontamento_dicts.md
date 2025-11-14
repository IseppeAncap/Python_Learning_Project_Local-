# Empacotamento desempacotamento com dicts + args kwargs
Esse resumo faz parte da aula 83

- Relembrando o asterisco `*` e seu uso. 
- Relembrando o asterisco `**` e seu uso.


- Não confuda `empacotamento (Packing) ,desempacotameto(Unpacking), necessariamente precisa de uma estar  acompanhados de uma função !
- O que é `args` e `Kwargs`

- Que raio são argumentos posicionais e  argumentos nomeados.

## O que seria um asterisco `*`!
 `Upacking` empacotamento 
 Quando você usa `*` em um **parametro de função** ele empacota varios argumentos em uma tupla!
Exemplo 
> def soma (* numeros)
>   return sum(numeros) # Pancking
>
> total = soma(1, 2, 3)
> print(total) # resultado 6

Você também pode usa - lo `*` para `Unpacking` **desempacotar argumentos**
Exemplo 
> numeros =(1, 2, 3, 4)
> print(* numeros) #  `Unpacking`Desempaconta
> 1 2 3 4 

------------------------------------------------------------------------
## O uso do asterisco duplo `**`
`Packing` Empacotamento.
Quando usado `**` em **argumentos nomeados** os chamados (kwargs) são empacotados em `dict`.

Exemplo

> def mostar_dados(** dados)
>    return dados

>processamento =mostrar_dados(nome=janio, idade=20)
>print(processamento) 
Saida
> {"nome":"janio", "idade": 20}

Você também pode usar para `Unpacking` desempacota-los.
> dados_usuario = {"nome":"janio", "idade": 20}
> def mostar_dados( dados)
>    return dados

>processamento =mostrar_dados(dados_usuario)
>print(**processamento) # Unpacking Desemapacotado

Saida

> "nome":"janio", "idade": 20
------------------------------------------------------
## 👉 Não depende de função pra acontecer.
 Não necessariamente o desempactamento precisa estár acompanhamnto de
`func` veremos alguns exeemplos abaixo .
# Packing sem o uso asterisco

a, b = 1, 2        # `Packing` normal
a, b = b, a        # troca usando `Packing` + `Unpacking` 
print(a, b)

# Até string podem ser Unpacking
letras = [janio]
print(*letras)
Saida
[j, a, n, i, o] 

# Juntando dicionarios 

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
pessoa_completa= {**pessoa, **dados_pessoas} #desempacontando em terceiro
print(pessoa_completa)


#### Fixe o que aprendemos sobre `Unpacking`, `Packing`
Desempacotar é espelahar valores
Podemos usar isso
. Na chamada funçaõ
. Na criação de listas, dicionarios.
. Na atribuição de valores
. em loops



----------------------------------------

