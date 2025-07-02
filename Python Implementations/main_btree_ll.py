from linear_structures.sll_tree import TreeSLL, TreeNode
from linear_structures.queue_tree import QueueTree
from non_linear_structures.btree_ll import BinaryTree

# ==== Tests ====
def test_sll_tree():
    """Tests the implementation of the SLL."""
    tree_sll = TreeSLL()
    print(tree_sll)

    print("Appending 5 elements in the SLL.")
    for i in range(1, 6):
        tree_sll.append(TreeNode(i * 6))
    print(tree_sll)

    print("Removing the five elements")
    popped_element: TreeNode
    for _ in range(5):
        popped_element = tree_sll.pop_first().value
        print("Popped Element: ", popped_element)
        print(tree_sll)

def test_queue_tree():
    """Tests the implementation of the Queue tree using SLL."""
    tree_queue: QueueTree = QueueTree()
    print(tree_queue)

    print("Appending 5 elements in the Queue")
    for i in range(1, 6):
        tree_queue.enqueue(i * 10)
    print(tree_queue)

    print("Removing the first 3 elements from the Queue")
    popped_element: TreeNode
    for _ in range(3):
        popped_element = tree_queue.dequeue().value
        print("Popped Element: ", popped_element)
        print(tree_queue)

    print("Appending another 5 elements in the Queue")
    for i in range(1, 6):
        tree_queue.enqueue(i * 6)
    print(tree_queue)

    new_tree_queue: QueueTree = QueueTree()
    print(f"Queue Tree 1 is empty ? -> {tree_queue.is_empty()}")
    print(f"Queue Tree 2 is empty ? -> {new_tree_queue.is_empty()}")

def test_btree():
    """Tests the functions and behaviour of the Binary Tree."""
    first_btree = BinaryTree()

    print("Adding 6 Children into the BTree.")
    for i in range(1, 7):
        first_btree.add_child(i * 10)
    print()
    print(first_btree)

    print("Here is the pre-order traversal")
    first_btree.pre_order_traversal(first_btree.root)
    print()
    print(first_btree)

    print("Here is in-order traversal")
    first_btree.in_order_traversal(first_btree.root)
    print()
    print(first_btree)
    
    print("Here is the post-order traversal")
    first_btree.post_order_traversal(first_btree.root)
    print()
    print(first_btree)

    print("Here is the level-order traversal")
    first_btree.level_order_traversal()
    print(first_btree)

    print("Searching for 10: ", first_btree.search_child(10))
    print("Searching for 60: ", first_btree.search_child(60))
    print("Searching for 600: ", first_btree.search_child(600), end="\n")

    print("Removing 30.")
    first_btree.remove_child(30)
    print(first_btree)
    print("Removing 10.")
    first_btree.remove_child(10)
    print(first_btree)


# ==== The Main Function ====
def main():
    test_sll_tree()
    print()
    test_queue_tree()
    print()
    test_btree()

# ==== Driver Code ====
if __name__ == "__main__":
    main()