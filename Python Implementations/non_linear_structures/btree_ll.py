from linear_structures.queue_tree import QueueTree
from linear_structures.sll_tree import TreeNode
from typing import Any, Generator


class BinaryTree:
    """This class implements all the behaviours of a Binary Tree."""
    # ==== Standard Methods ====
    def __init__(self) -> None:
        self.root: TreeNode | None = None
        self.no_of_elements: int = 0
        self.frontier = QueueTree()

    def __str__(self) -> str:
        """Provides a string repr for the tree."""
        repr_str: str = self.print_tree(self.root)
        return repr_str
    
    def __iter__(self) -> Generator[Any, None, None]:
        """Provides an iterator to traverse the nodes of the Binary Tree in Level Order."""
        if not self.root:
            raise IndexError("Iterator cannot be generated for an empty tree.")
        else:
            # Clearing the Frontier before usage
            self.frontier.clear()

            # Beginning level order traversal
            self.frontier.enqueue(self.root)
            current_node: TreeNode
            while not self.frontier.is_empty():
                current_node = self.frontier.dequeue().value
                yield current_node

                # Updating the Frontier for follow-up nodes.
                if current_node.left_child:
                    self.frontier.enqueue(current_node.left_child)
                if current_node.right_child:
                    self.frontier.enqueue(current_node.right_child)

    # ==== Member Functions ====
    def print_tree(self, node: TreeNode | None, level: int = 0, label: str = "Root:") -> str:
        """Creates a string repr of the tree."""
        # If the tree is empty.
        if not node:
            return ""
        # If the tree is not empty.
        right = self.print_tree(node.right_child, level + 1, "R---")
        curr_str = "       " * level + f"{label} {node.value}\n"
        left = self.print_tree(node.left_child, level + 1, "L---")

        return right + curr_str + left
    
    def pre_order_traversal(self, node: TreeNode | None) -> None:
        """Performs pre order traversal on the Binary Tree."""
        # If the tree is empty.
        if self.no_of_elements == 0:
            raise IndexError("The tree is currently empty.")
        # If the tree is not empty.
        else:
            if not node:
                return
            print(node)
            self.pre_order_traversal(node.left_child)
            self.pre_order_traversal(node.right_child)

    def in_order_traversal(self, node: TreeNode | None) -> None:
        """Performs level order traversal on the Binary Tree."""
        # If the tree is empty.
        if self.no_of_elements == 0:
            raise IndexError("The tree is currently empty.")
        # If the tree is not empty.
        else:
            if not node:
                return
            self.in_order_traversal(node.left_child)
            print(node)
            self.in_order_traversal(node.right_child)
    
    def post_order_traversal(self, node: TreeNode | None) -> None:
        """Performs post order traversal on the Binary Tree."""
        # If the tree is empty.
        if self.no_of_elements == 0:
            raise IndexError("The tree is currently empty.")
        # If the tree is not empty.
        else:
            if not node:
                return
            self.post_order_traversal(node.left_child)
            self.post_order_traversal(node.right_child)
            print(node)

    def level_order_traversal(self) -> None:
        """Performs level order traversal on the Binary Tree."""
        # If the tree is empty.
        if not self.root:
            raise IndexError("The tree is currently empty.")
        # If the tree is not empty.
        else:
            # Clearing the Common Frontier
            self.frontier.clear()

            # Enter the root node to the queue to begin traversal.
            self.frontier.enqueue(self.root)
            
            # Begin Traversal from the root node recursively until the queue is empty again.
            while not self.frontier.is_empty():
                current_node: TreeNode = self.frontier.dequeue().value
                print(current_node)
                if current_node.left_child:
                    self.frontier.enqueue(current_node.left_child)
                if current_node.right_child:
                    self.frontier.enqueue(current_node.right_child)

    def add_child(self, value: Any) -> None:
        """Adds a new child to the tree."""
        new_node: TreeNode = TreeNode(value)

        # If the tree is empty
        if not self.root:
            self.root = new_node
        else:
            # Clearing the Common Frontier
            self.frontier.clear()

            # Starting Level Order Traversal to Find Location for Insertion.
            self.frontier.enqueue(self.root)
            current_node: TreeNode
            while not self.frontier.is_empty():
                current_node = self.frontier.dequeue().value
                if not current_node.left_child:
                    current_node.left_child = new_node
                    break
                elif not current_node.right_child:
                    current_node.right_child = new_node
                    break
                else:
                    self.frontier.enqueue(current_node.left_child)
                    self.frontier.enqueue(current_node.right_child)
            
        # Updating the no of elements in the tree.
        self.no_of_elements += 1
        
    def search_child(self, value: Any) -> bool:
        """Returns a boolean for the first occurence of the value."""
        for node in self:
            if node.value == value:
                return True
            elif node.left_child and node.left_child.value == value:
                return True
            elif node.right_child and node.right_child.value == value:
                return True
        return False
    
    def get_child(self, value: Any) -> TreeNode:
        """Returns the treenode for a given value."""
        get_node: TreeNode
        for node in self:
            if node and node.value == value:
                get_node = node
                return get_node
        else:
            raise ValueError("The requested value doesn't exist in the tree.")
        
    def get_deepest_node(self) -> TreeNode:
        """Returns the deepest node in the tree."""
        deepest_node: TreeNode | None = None
        for node in self:
            if node:
                deepest_node = node

        assert deepest_node, "Deepest node cannot be none in Level Order Traversal."
        return deepest_node
    
    def remove_deepest_node(self, deepest_node: TreeNode):
        """Prunes the deepest node from the tree."""
        for node in self:
            if node and node.left_child is deepest_node:
                node.left_child = None
                return
            elif node and node.right_child is deepest_node:
                node.right_child = None
                return
            else:
                continue
    
    def remove_child(self, value: Any) -> None:
        """Search for given value in the children of the tree, remove it and return it."""
        if not self.root:
            raise IndexError("The tree has no more children to be removed.")

        # Retrieving the required nodes.
        remove_node: TreeNode = self.get_child(value)
        deepest_node: TreeNode = self.get_deepest_node()

        # Checking the nodes
        if not remove_node or not deepest_node:
            raise ValueError("Node to be removed or the deepest node couldn't be found.")
        
        # If only one node is left in the tree.
        if remove_node is deepest_node:
            self.remove_deepest_node(deepest_node)
            self.no_of_elements -= 1
            return
        # If there are more than one nodes left in the tree.
        remove_node.value = deepest_node.value
        self.remove_deepest_node(deepest_node)
        self.no_of_elements -= 1



        

        

        
