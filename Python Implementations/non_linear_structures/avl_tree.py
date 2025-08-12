from linear_structures.queue_tree import QueueTree
from non_linear_structures.avl_node import AVLNode
from typing import Any, Generator


class AVLTree:
    """Implements the properties and behaviour of an AVL tree."""
    # ==== Standard Methods ====
    def __init__(self) -> None:
        self.root: AVLNode | None = None
        self.no_of_elements: int = 0
        self.frontier: QueueTree = QueueTree()

    def __str__(self) -> str:
        """Provides a string representation for the AVL Tree."""
        return self.print_tree(self.root)
    
    def __iter__(self) -> Generator[AVLNode | None, None, None]:
        """Provides an iterator to the AVL Tree using Level Order Traversal."""
        if not self.root:
            raise IndexError("The tree is empty, cannot generate an iterator, add new elements.")
        
        # Performing Level Order Traversal
        remove_node: AVLNode
        self.frontier.clear()
        self.frontier.enqueue(self.root)
        while not self.frontier.is_empty():
            remove_node = self.frontier.dequeue().value
            yield remove_node

            # If Children exist continue traversal
            if remove_node.left_child:
                self.frontier.enqueue(remove_node.left_child)
            if remove_node.right_child:
                self.frontier.enqueue(remove_node.right_child)

    # ==== Member Functions ====
    def add_child(self, node: AVLNode | None, new_node: AVLNode):
        """
        Adds a new value to the AVL Tree in two steps:
        1. Finds a vacancy using Binary Search Tree principles.
        2. Applies rotations if needed based on the case of the rotation required.
        """
        # Step 1. Inserting the new node
        # If the tree is empty.
        if not self.root:
            self.root = new_node
            self.no_of_elements += 1
            return
        # Adding the new node as the left child.
        assert node, "Node cannot be none in the middle of the tree."
        if node.value > new_node.value:
            if node.left_child:
                self.add_child(node.left_child, new_node)
            else:
                node.left_child = new_node
                self.no_of_elements += 1
        # Adding the new node as the right child.
        else:
            if node.right_child:
                self.add_child(node.right_child, new_node)
            else:
                node.right_child = new_node
                self.no_of_elements += 1

        # Step 2. Balancing the Node if necessary
        self.root.height = max(self.get_height(self.root.left_child), self.get_height(self.root.right_child))
        balance = self.get_balance(self.root)
        
    # ==== Helper Functions ====
    def print_tree(self, node: AVLNode | None, label: str = "Root: ", level: int = 0) -> str:
        """Provides a string representation for the entire tree."""
        # If the tree is empty.
        if not self.root:
            return "None <= Root"
        
        # If the tree is not empty.
        assert node, "The node cannot be none in the middle of the tree."
        right: str = ""
        current: str = ""
        left: str = ""

        if node.right_child:
            right = self.print_tree(node.right_child, "R----", level + 1)
        if node.left_child:
            left = self.print_tree(node.left_child, "L----", level + 1)
        current = "       " * level + f"{label} {node.value}\n"

        return right + current + left

    def get_height(self, node: AVLNode | None):
        """Calculates the height of any given node in the AVLTree."""
        if not node:
            return 0
        return node.height
    
    def get_balance(self, node: AVLNode | None):
        """Provide the difference of the Height at any given Node."""
        
        # If the node is none.
        if not node:
            return 0
        
        # If the node is not none.
        return self.get_height(node.left_child) - self.get_height(node.right_child)
        

    def right_rotate(self, disbalanced_node: AVLNode | None):
        """Implements the right rotation for balancing the AVL Tree."""
        
        # If the disbalanced node is none.
        if not disbalanced_node:
            return
        
        # If the disbalanced node is not none.
        new_root = disbalanced_node.left_child
        disbalanced_node.left_child = (
            disbalanced_node.left_child.right_child if disbalanced_node.left_child else None
        )
        new_root.right_child = disbalanced_node  # type: ignore

        # Updating the height
        disbalanced_node.height = 1 + max(self.get_height(disbalanced_node.left_child), self.get_height(disbalanced_node.right_child))
        new_root.height = 1 + max(self.get_height(new_root.left_child), self.get_height(new_root.right_child))  # type: ignore

        return new_root
    
    def left_rotate(self, disbalanced_node: AVLNode | None):
        """Implements the left rotation for balancing the AVL Tree."""

        # If the disbalanced node is none.
        if not disbalanced_node:
            return
        
        # If the disbalanced node is not none.
        new_root = disbalanced_node.right_child
        disbalanced_node.right_child = (
            disbalanced_node.right_child.left_child if disbalanced_node.right_child else None
        )
        new_root.left_child = disbalanced_node  # type: ignore

        # Updating the height
        disbalanced_node.height = 1 + max(self.get_height(disbalanced_node.left_child), self.get_height(disbalanced_node.right_child))
        new_root.height = 1 + max(self.get_height(new_root.left_child), self.get_height(new_root.right_child))  # type: ignore

        return new_root
    


    