from non_linear_structures.avl_node import AVLNode
from non_linear_structures.avl_tree import AVLTree


# The main function
def main():
    first_avl_tree = AVLTree()
    
    for i in range(-4, 5):
        first_avl_tree.root = first_avl_tree.add_child(first_avl_tree.root, AVLNode(i))
        print(f"Tree after Adding the Child {i}")
        print(first_avl_tree.print_tree(first_avl_tree.root))

    nodes_to_del = [4, 0, -1, 2]
    for node in nodes_to_del:
        first_avl_tree.root = first_avl_tree.delete_child(first_avl_tree.root, node)
        print(f"Tree after Removing the Child {node}")
        print(first_avl_tree.print_tree(first_avl_tree.root))


# Driver Code
if __name__ == "__main__":
    main()