"""
CP1404/CP5632 Practical
Testing/example client code for trees classes
When you complete all the subclasses, you'll see that they behave differently.

"""
import prac_08.trees as trees


def main():
    """Program to demonstrate trees of different types."""
    # Let's make some trees of different classes (subclasses)
    tree_list = [trees.Tree(), trees.EvenTree(), trees.UpsideDownTree(),
                 trees.WideTree(), trees.QuickTree(), trees.FruitTree(),
                 trees.PineTree()]

    # display all the trees
    for tree in tree_list:
        print(tree.__class__)
        print(tree)

    print("Time to grow!")
    # grow them several times
    for _ in range(5):
        for tree in tree_list:
            tree.grow(5, 2)

    # display all the trees again
    for tree in tree_list:
        print(tree.__class__)
        print(tree)


main()
