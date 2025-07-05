from non_linear_structures.binary_search_tree import BinarySearchTree
from non_linear_structures.btree_ll import TreeNode
import random

# ==== The Main Function ====
def main():
    bst = BinarySearchTree()

    print("Appending 7 elements into the tree.")
    elements = [i for i in range(1, 8)]
    random.shuffle(elements)
    print("Insertion Order: ", elements)
    for i in elements:
        bst.add_child(bst.root, TreeNode(i * 10))
    print(bst)

    print("Removing 50")
    bst.delete_child(bst.root, 50)
    print(bst)

    print("Searching for 20: ", bst.search(bst.root, 20))
    print("Searching for 30: ", bst.search(bst.root, 30))
    print("Searching for 60: ", bst.search(bst.root, 60))
    print("Searching for 100: ", bst.search(bst.root, 100))
    print("Searching for -200: ", bst.search(bst.root, -200))

    print("\nPerforming Pre-Order traversal on the tree.")
    bst.pre_order(bst.root)

    print("\nPerforming In-Order traversal on the tree.")
    bst.in_order(bst.root)

    print("\nPerforming Post-Order traversal on the tree.")
    bst.post_order(bst.root)

    print("\nPerforming a Level-Order traversal on the tree.")
    bst.level_order()

# ==== Driver Code ====
if __name__ == "__main__":
    main()