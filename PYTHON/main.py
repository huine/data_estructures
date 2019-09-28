# from Estoque import Estoque

# estoque = Estoque()

# estoque.cadastrar_mercadoria('teste', 15.25, 5, 1)

# for item in estoque.lista_mecadoria:
#     print(item)

from HashTable import HashTable

h = HashTable()

h.put('teste', 156546)
h.put('weqweq', 6756756)
h.put('tertert', 89089)
h.put('jkhjkhjkh', 12312)
h.put('sdasdas', 12345678909876543)
h.put('sdasdas', 99999)

for item in h:
    print(item)