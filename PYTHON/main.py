from HashTable import HashTable

h = HashTable()

h['a'] = 'teste a'
h[44] = 'teste 44'
h['b'] = 'teste b'
h[31] = 'teste 31'
h['c'] = 'teste c'
h[14] = 'teste 14'
h['e'] = 'teste e'
h[84] = 'teste 84'
h['f'] = 'teste f'
h[71] = 'teste 71'

print(h)
print(h.get('a'))


del h[71]

print(h)
