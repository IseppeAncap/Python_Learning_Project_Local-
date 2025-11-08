
lista = [
    {'nome': 'Luiz', 'sobrenome': 'miranda'},
    {'nome': 'Maria', 'sobrenome': 'Oliveira'},
    {'nome': 'Daniel', 'sobrenome': 'Silva'},
    {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
    {'nome': 'Aline', 'sobrenome': 'Souza'},
]

# detalhes sobre o codigo inteiro no Readme_otimizando_com_lambda.md 

def exibir(lista):
    for item in lista:
        print(item)
    print() # pula uma linha ao final de cada matriz

# Ordena as listas pro chave valor
nome = sorted(lista, key= lambda item : item['nome'])
sobrenome = sorted(lista, key= lambda item : item['sobrenome'])
# chama a função com paramtros já ordenados exibi 
print('Ordena pelo nome:')
exibir(nome)
print('Ordena pelo sobrenome')
exibir(sobrenome)