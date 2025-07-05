from linear_structures.queue_tree import QueueTree
from non_linear_structures.btree_ll import TreeNode
from typing import Any, Generator


class BinarySearchTree:
    """Implements the structure and methods of a Binary Search Tree."""
    # ==== Standard Methods ====
    def __init__(self) -> None:
        self.root: TreeNode | None = None
        self.no_of_elements: int = 0
        self.frontier = QueueTree()

    def __str__(self) -> str:
        """Provides a string representation of the tree."""
        if not self.root:
            raise IndexError("The Tree is empty, add new element for visualisation.")
        else:
            return self.print_tree(self.root)
        
    def __iter__(self) -> Generator[TreeNode | None, None, None]:
        """Provides an iterator for the Binary Search tree using level order traversal."""
        if not self.root:
            raise IndexError("The Binary Search Tree is empty, add new elements to generate iterator.")
        
        # Clear the Frontier
        self.frontier.clear()
        self.frontier.enqueue(self.root)
        
        # Level-Order Traversal
        current_element: TreeNode
        while not self.frontier.is_empty():
            current_element = self.frontier.dequeue().value
            yield current_element

            # Adding elements from the next level
            if current_element.left_child:
                self.frontier.enqueue(current_element.left_child)
            if current_element.right_child:
                self.frontier.enqueue(current_element.right_child)

    # ==== Helper Functions ====
    def print_tree(self, node: TreeNode, level: int = 0, label: str = "root: ") -> str:
        """Constructs a string representation for the tree."""
        if not node:
            return ""
        
        left: str = ""
        right: str = ""
        current: str = ""
        
        # Traversing the left subtree
        if node.left_child:
            left = self.print_tree(node.left_child, level + 1, "L----")
        # Traversing the right subtree
        if node.right_child:
            right = self.print_tree(node.right_child, level + 1, "R----")
        current = "            " * level + f"{label} {node.value}\n"

        return right + current + left
    
    @staticmethod
    def get_min_value(node: TreeNode) -> TreeNode:
        """Returns the smallest node for minimum value extraction."""
        cursor: TreeNode = node
        while cursor.left_child is not None:
            cursor = cursor.left_child
        return cursor
    
    # ==== Member Functions ====
    def add_child(self, root_node: TreeNode | None, new_node: TreeNode) -> None:
        """Adds a new child to the tree."""
        # If the tree is empty.
        if not self.root:
            self.root = new_node
            # Update the no of elements
            self.no_of_elements += 1
            return
        
        # If the value of the new_node is <= root_node traverse left.
        assert root_node, "Root node cannot be none."
        if new_node.value <= root_node.value:
            # If left child doesn't exist allocate.
            if not root_node.left_child:
                root_node.left_child = new_node
                # Update the no of elements
                self.no_of_elements += 1
                return
            # If left child exists traverse further.
            else:
                self.add_child(root_node.left_child, new_node)
        # If the value of the new_node is > root_node traverse right.
        else:
            # If right child doesn't exist allocate.
            if not root_node.right_child:
                root_node.right_child = new_node
                # Update the no of elements
                self.no_of_elements += 1
                return
            else:
                self.add_child(root_node.right_child, new_node)

    def delete_child(self, root_node: TreeNode | None, value: Any) -> TreeNode | None:
        """Removes a child for the tree identified by the first occurence of the value."""
        # If the tree is empty.
        if not root_node:
            return root_node
        # If the value is less than the root_node traverse left.
        if value < root_node.value:
            root_node.left_child = self.delete_child(root_node.left_child, value)
        # If the value is greater than root_node traverse right.
        elif value > root_node.value:
            root_node.right_child = self.delete_child(root_node.right_child, value)
        # If not both then arrived at node in question to perform deletion based on cases.
        else:
            # If the current root_node has atleast one child or none.
            temp: TreeNode | None = None
            # Case - 1: If the one child is on the right or none.
            if root_node.left_child is None:
                temp = root_node.right_child
                root_node = None
                
                # Update the no of nodes in the tree
                self.no_of_elements -= 1
                return temp
            
            # Case - 2: If the one child is on the left or none.
            if root_node.right_child is None:
                temp = root_node.left_child
                root_node = None
                
                # Update the no of nodes in the tree
                self.no_of_elements -= 1
                return temp
            
            # If the root_has two children
            temp = BinarySearchTree.get_min_value(root_node.right_child)
            root_node.value = temp.value
            root_node.right_child = self.delete_child(root_node.right_child, temp.value)

        # Returns the update branch
        return root_node

    def search(self, root_node: TreeNode | None, value: Any) -> bool:
        """Returns a boolean on finding the first occurence of the given element."""
        if not self.root:
            raise IndexError("The tree is empty, add new elements to perform subsequent ops.")
        
        # If root node is the value being searched
        if not root_node:
            return False
        elif root_node.value == value:
            return True
        # If value is lesser than the root node traverse left.
        elif value < root_node.value:
            if root_node.left_child:
                return self.search(root_node.left_child, value)
            return False
        # If the value is greater than root node traverse right.
        else:
            if root_node.right_child:
                return self.search(root_node.right_child, value)
            return False
    
    # ==== Tree Traversals ====
    def pre_order(self, root_node: TreeNode | None) -> None:
        """Performs a pre-order traversal on the tree."""
        if not self.root:
            raise IndexError("The tree is empty, add new elements before traversal.")
        
        # If the traversal reaches the leaf node.
        if not root_node:
            return
        # Print the current root_node
        print(root_node)
        # Print the left subtree
        self.pre_order(root_node.left_child)
        # Print the righ subtree
        self.pre_order(root_node.right_child)

    def in_order(self, root_node: TreeNode | None) -> None:
        """Performs a in-order traversal on the tree."""
        if not self.root:
            raise IndexError("The tree is empty, add new elements before traversal.")
        
        # If the traversal reaches the leaf node.
        if not root_node:
            return
        # Print the left subtree
        self.in_order(root_node.left_child)
        # Print the current root_node
        print(root_node)
        # Print the righ subtree
        self.in_order(root_node.right_child)

    def post_order(self, root_node: TreeNode | None) -> None:
        """Performs a post-order traversal on the tree."""
        if not self.root:
            raise IndexError("The tree is empty, add new elements before traversal.")
        
        # If the traversal reaches the leaf node.
        if not root_node:
            return
        # Print the left subtree
        self.post_order(root_node.left_child)
        # Print the righ subtree
        self.post_order(root_node.right_child)
        # Print the current root_node
        print(root_node)

    def level_order(self) -> None:
        """Performs a level-order traversal on the tree."""
        if not self.root:
            raise IndexError("The Binary Search Tree is empty, add new elements to generate iterator.")
        
        # Clear the Frontier
        self.frontier.clear()
        self.frontier.enqueue(self.root)
        
        # Level-Order Traversal
        current_element: TreeNode
        while not self.frontier.is_empty():
            current_element = self.frontier.dequeue().value
            print(current_element)

            # Adding elements from the next level
            if current_element.left_child:
                self.frontier.enqueue(current_element.left_child)
            if current_element.right_child:
                self.frontier.enqueue(current_element.right_child)
