from AVL import AVLTree
from random import randrange

avl = AVLTree()

for i in range(20):
    avl.insert(randrange(0, 1000))

print(avl)
