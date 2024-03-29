import random

from bTree import bTree

print("Creating Binary Tree")
t = bTree(1)

print("Adding elements to the tree")
t.addList(random.sample(xrange(50), 50))

print("Printing Tree")
t.printTree()

p = t.findPathLength()
print("Internal Path Length (P):" + str(p))

n = t.count()
print("Number of nodes (N): " + str(n))

r = float(p) / float(n)
print("Average path length (P/N): " + str(r))
