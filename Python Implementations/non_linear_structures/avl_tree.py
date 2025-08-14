from linear_structures.queue_tree import QueueTree
from non_linear_structures.avl_node import AVLNode
from typing import Generator


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
        # If leaf node is reached
        if not node:
            self.no_of_elements += 1
            return new_node
        # Adding the new node as the left child.
        if node.value > new_node.value:
            node.left_child = self.add_child(node.left_child, new_node)
        # Adding the new node as the right child.
        else:
            node.right_child = self.add_child(node.right_child, new_node)
            
        # Step 2. Updating the height of the nodes based on the backtrack after insertion using recursion.
        node.height = 1 + max(self.get_height(node.left_child), self.get_height(node.right_child))

        # Step 3. Get the balance for balancing the tree.
        balance = self.get_balance(node)
        
        # Step 4. Balancing the AVL Tree.
        # ==== Left - Heavy Cases ====
        # LL Condition
        if balance > 1 and node.left_child and new_node.value < node.left_child.value:
            return self.right_rotate(node)
        # LR Condition
        if balance > 1 and node.left_child and new_node.value > node.left_child.value:
            node.left_child = self.left_rotate(node.left_child)
            return self.right_rotate(node)
        
        # ==== Right Heavy Cases ====
        # RR Condition
        if balance < -1 and node.right_child and new_node.value > node.right_child.value:
            return self.left_rotate(node)
        # RL Condition
        if balance < -1 and node.right_child and new_node.value < node.right_child.value:
            node.right_child = self.right_rotate(node.right_child)
            return self.left_rotate(node)
        
        # Returning the changed node for Recursive Propagation
        return node
    
    def delete_child(self, node: AVLNode | None, delete_value: int):
        """Deletes a child from the tree."""
        
        # Step 1. Deleting the node
        # If the tree is empty or If left node was reached when searching for the delete value
        if not node:
            return node
        # If the delete value < node: Traversing Left
        if node.value > delete_value:
            node.left_child = self.delete_child(node.left_child, delete_value)
        # If the delete value > node: Traversing Right
        elif node.value < delete_value:
            node.right_child = self.delete_child(node.right_child, delete_value)
        # If the delete value is reached.
        else:
            temp: AVLNode | None = None

            # If the delete node has at most one child on the right
            if node.left_child is None:
                temp = node.right_child

                # Updating the no of elements
                self.no_of_elements -= 1
                return temp
            
            # If the delete node has at most one child on the right
            elif node.right_child is None:
                temp = node.left_child

                # Updating the no of elements
                self.no_of_elements -= 1
                return temp
            
            # If the delete node has two children
            temp = AVLTree.get_minimum_node(node.right_child)
            node.value = temp.value
            node.right_child = self.delete_child(node.right_child, temp.value)

        # If the last node in the tree was deleted
        if not node:
            return node
        
        # Step 2. Updating the height
        node.height = 1 + max(self.get_height(node.left_child), self.get_height(node.right_child))

        # Step 3. Checking for the need of balancing
        balance = self.get_balance(node)

        # Step 4. Balancing the tree if the node is unbalanced
        # Left Heavy Cases
        if balance > 1 and node.left_child:
            balance_left = self.get_balance(node.left_child)
            # LL Condition
            if balance_left >= 0:
                return self.right_rotate(node)
            # LR Condition
            else:
                node.left_child = self.left_rotate(node.left_child)
                return self.right_rotate(node)
        # Right Heavy Cases
        if balance < -1 and node.right_child:
            balance_right = self.get_balance(node.right_child)
            # RR Condition
            if balance_right <= 0:
                return self.left_rotate(node)
            # RL Condition
            else:
                node.right_child = self.right_rotate(node.right_child)
                return self.left_rotate(node)

        # Returns the updated and balanced node
        return node            
        
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
        current = "           " * level + f"{label} {node.value}\n"

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
    
    @staticmethod
    def get_minimum_node(root_node: AVLNode):
        """Finds the minimum node wrt a given root node."""
        min_node: AVLNode = root_node
        while min_node.left_child is not None:
            min_node = min_node.left_child
        return min_node
    
    def get_remove_node(self, node: AVLNode, value: int):
        """Finds the node to be removed by value."""
        if node.value == value:
            return node
        elif node.left_child and node.value > value:
            return self.get_remove_node(node.left_child, value)
        elif node.right_child and node.value < value:
            return self.get_remove_node(node.right_child, value)
        else:
            raise ValueError("The node to be removed doesn't exist in the tree.")