# exemplos de codigo da aula 83.

pessoa = { 
    "nome": "Aline",
    "sobrenome": "Souza",
}
# desempacotando dicionários em variáveis
(a1, a2 ), (b1, b2)= pessoa.items()
print(a1, a2, b1 , b2)

dados_pessoas = {
    "altura": 1.60,
    "idade": 28
}

# junção de dicts 
pessoa_completa = {}
pessoa_completa= {**pessoa, **dados_pessoas}
print(pessoa_completa)

 

# Demonstração de argumentos posicionais e nomeados
def mostro_argumentos_nomeados(*args,**kwargs ):
    print(f'não nomeados = {args}')
    
    for chave , valor in kwargs.items():
        print(chave, valor )
        print('----')
mostro_argumentos_nomeados(2,5,6, nome= 'janio', frutas= 'coco')

# Exemplo de desempacotamento na chamada da função 
dado = {
    'a': 1,
    'b': 33
}
def f(a, b):
    print(a, b)
f(**dado)

# exemplo desempacotamento e empacotamentos sem o uso de operadores !

a , b = 1 , 2
a , b = b , a
print(a, b)