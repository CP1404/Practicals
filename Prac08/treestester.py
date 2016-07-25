"""
CP1404/CP5632 Practical
Testing/example client code for trees classes
"""
import Prac08.trees as trees

# let's make some trees
treeList = [trees.Tree(), trees.EvenTree(), trees.UpsideDownTree(),
            trees.WideTree(), trees.QuickTree(), trees.FruitTree(),
            trees.PineTree()]

# display all the trees
for tree in treeList:
    print(tree.__class__)
    print(tree)

print("Time to grow!")
# grow them several times
for i in range(5):
    for tree in treeList:
        tree.grow(5, 2)

# display all the trees again
for tree in treeList:
    print(tree.__class__)
    print(tree)

# when you complete all the subclasses, you'll see that they behave differently
