from Estoque import Estoque

estoque = Estoque()

estoque.cadastrar_mercadoria('teste', 15.25, 5, 1)

for item in estoque.lista_mecadoria:
    print(item)
