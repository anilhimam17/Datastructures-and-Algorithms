from non_linear_structures.btree_list import BinaryTree

# ==== The Main Function ====
def main():
    list_btree = BinaryTree()

    print("Adding 5 new children into the Binary Tree.")
    for i in range(1, 8):
        list_btree.add_child(i * 10)
    print(list_btree)

    print("Removing 20")
    list_btree.remove_child(20)
    print(list_btree)
    print("Removing 30")
    list_btree.remove_child(30)
    print(list_btree)

    print("Searching for 10: ", list_btree.search_child(10))
    print("Searching for 70: ", list_btree.search_child(70))
    print("Searching for 1000: ", list_btree.search_child(1000))

    list_btree.update_child(70, 1000)
    print("Searching for 1000: ", list_btree.search_child(1000))
    print(list_btree)

    new_binary_tree = BinaryTree(10)
    for i in range(1, 8):
        new_binary_tree.add_child(i * 10)
    print(new_binary_tree)

    print("Here is the pre-order traversal of the Binary Tree.")
    new_binary_tree.preorder_traversal(1)

    print("Here is the in-order traversal of the Binary Tree.")
    new_binary_tree.inorder_traversal(1)

    print("Here is the post order traversal of the Binary Tree.")
    new_binary_tree.postorder_traversal(1)

# ==== Driver Code ====
if __name__ == "__main__":
    main()