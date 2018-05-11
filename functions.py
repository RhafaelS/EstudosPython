def add_lista(anything):
    lista = []

    while anything:
        print("Lista antiga: {}".format(anything))
        dados = anything.pop()
        lista.append(dados)
        print("Lista nova: {}".format(lista))

    return lista

itens = []

while len(itens) != 10 :
    param = input("Digite até 10 itens ou digite 'no' para finalizar: ")
    if param != 'no':
        itens.append(param)
    else:
        print("Fechou os itens!")
        break

add_lista(itens)

