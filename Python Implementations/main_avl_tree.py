from non_linear_structures.avl_node import AVLNode
from non_linear_structures.avl_tree import AVLTree


# The main function
def main():
    first_avl_tree = AVLTree()
    
    print("Appeding 5 children into the tree without rotations.")
    for i in range(5):
        first_avl_tree.add_child(first_avl_tree.root, AVLNode(i))
    print(first_avl_tree.print_tree(first_avl_tree.root))


# Driver Code
if __name__ == "__main__":
    main()