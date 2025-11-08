# Aula parte 1: Entedendo como key e sort  funcionam func ordenação
# para mais detalhes ler Readmen
lista = [
    {'nome': 'Luiz', 'sobrenome': 'miranda'},
    {'nome': 'Maria', 'sobrenome': 'Oliveira'},
    {'nome': 'Daniel', 'sobrenome': 'Silva'},
    {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
    {'nome': 'Aline', 'sobrenome': 'Souza'},
]
def ordena(item):
    print(item)
    return item['sobrenome']

lista.sort(key=ordena) 

for item in lista:
    print(item)

