from AVL import AVLTree
from random import randrange, choice

avl = AVLTree()
r = [randrange(1, 10000) for i in range(1000)]
search = choice(r)
for i in r:
    avl.insert(i)

# print(avl)
print("Min List: %s" % (min(r)))
print("Max List: %s" % (max(r)))
print("Min Tree: %s" % (avl.find_min().value))
print("Max Tree: %s" % (avl.find_max().value))
print("Item find List: %s" % (search))
print("Item find Tree: %s" % (avl.find(11000)))
