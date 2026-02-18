from non_linear_structures.trie_node import TrieNode


class Trie:
    """This structure implements all the properties of a Trie Datastructure."""

    def __init__(self) -> None:
        self.root: TrieNode | None = None

    def __str__(self) -> str:
        """Provides a string representation for the Trie."""
        return self.print_trie(self.root)
    
    def print_trie(self, node: TrieNode | None, level: int = 0) -> str:
        """Provides a pretty representation of the Trie."""

        # If Trie is empty
        if not self.root:
            return "None <= Root"
        
        assert node, "Trie Node cannot be None in the Middle of the Trie"
        current: str = ""
        children: str = ""

        if node.children:
            for key in node.children.keys():
                children += self.print_trie(node=node.children[key], level=level+1)
        
        current = "         " * level + f"---- {node.value} {node.EOF}\n"
        return current + children

    def insert(self, input_string: str) -> None:
        """Performs the insertion operation to populate the Trie."""
        
        # If the Trie is empty
        if self.root is None:
            self.root = TrieNode(value=input_string[0])
        # If the Trie is not empty but Prefix is different
        if self.root and (input_string[0] not in self.root.value):
            self.root.value.append(input_string[0])

        # If the Trie is not empty and Prefix matches
        # Node tracking while traversing the Trie
        current_node: TrieNode = self.root
        # Iterating through the characters of the string
        for i in range(1, len(input_string)):
            
            # Accessing the next character
            ch: str = input_string[i]

            # If next character already in Trie corpus
            if ch in current_node.children.keys():
                current_node = current_node.children[ch]
            # If next character not in Trie corpus
            else:
                current_node.children[ch] = TrieNode(ch)
                current_node = current_node.children[ch]

            # Adding EOF
            if i == len(input_string) - 1:
                current_node.EOF = True
