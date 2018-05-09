itens = ['pedra', 'papel', 'tesoura', 'galho', 'faca', 'marreta']


def add_lista(anything):
    lista = []

    for item in anything:
        print(anything)
        dados = anything.pop()
        lista.append(dados)
        print(lista)

add_lista(itens)


""""
while itens:
    param = input("Digite um item ou digite 'no' para finalizar: ")
    if param != 'no':
        itens.append(param)
    else:
        print("Fechou os itens!")
        break

"""

