from non_linear_structures.trie_node import TrieNode


class Trie:
    """This class implements all the properties of a Trie Datastructure."""

    def __init__(self) -> None:

        # Root Node is a Dummy Node by default navigating to different string
        # through its children instance variable.
        self.root: TrieNode = TrieNode()

    def __str__(self) -> str:
        """Provides a string representation for the Trie."""

        # If Trie is empty
        if not self.root.children:
            return "None <= Root"

        # If Trie is not empty
        return self.print_trie(self.root)
    
    def print_trie(self, node: TrieNode, label: str = "*", level: int = 0) -> str:
        """Provides a pretty representation of the Trie."""
        
        # Cumulative String for reducing the heirarchy of the Trie Recursively
        current: str = ""
        children: str = ""

        # Base Case: Stops if not children are present at current node
        if node.children:
            for key in node.children.keys():
                # Recursive Case: Keeps Traversing Top-Down till leaf nodes
                children += self.print_trie(node=node.children[key], label=key, level=level+1)
        
        current = "       " * 2 * level + f"---- ({label} | {node.EOF})\n"
        return current + children

    def insert(self, input_string: str) -> None:
        """Performs the insertion operation to populate the Trie."""

        # The input string shouldn't be empty
        if input_string:
            
            # Top Most node to begin insertion
            current_node = self.root
            
            # Traversing through the characters of the input string for insertion
            for ch in input_string:
                
                # If the character is not in Current Node's Children
                if ch not in current_node.children:
                    current_node.children[ch] = TrieNode()
                    current_node: TrieNode = current_node.children[ch]
                # If first character in Current Node's Children
                else:
                    current_node: TrieNode = current_node.children[ch]

            # Adding EOF
            current_node.EOF = True
    
    def search(self, input_string: str) -> bool:
        """Performs the search operation on the Trie to check for
        the existence of Input String in the Trie's corpus."""
        
        # Top Most Node to begin Search
        current_node: TrieNode = self.root

        # If the Trie is empty
        if not current_node.children:
            return False
        
        # If the Trie is not empty
        for ch in input_string:
            # Check if prefix in current node's children to continue search
            if ch not in current_node.children:
                return False
            else:
                current_node = current_node.children[ch]

        # If loop successful check for EOF at last character for existence of the word
        return current_node.EOF
    
    def starts_with(self, input_seed: str) -> list[str] | bool:
        """Performs the Autocomplete functionality for searching a Trie's corpus
        based on input_seed to provide suggested list of strings."""

        # Top Most Node to begin Search
        current_node: TrieNode = self.root

        # If the Trie is empty
        if not current_node.children:
            return False

        # Iterating through the Seed to reach the node in the Trie so explore String Suffixes
        for ch in input_seed:
            # If the Seed Character not in Children the String doesn't exist in the Trie
            if ch not in current_node.children:
                return False
            else:
                current_node = current_node.children[ch]

        # List to store all the autocomplete substrings
        plausible_strs: list[str] = []

        # Performing the exploration for all possible strings from the Last TrieNode
        plausible_strs = Trie._find_all_from_node(
            node=current_node,
            current_word_prefix=input_seed,
            words_discovered=plausible_strs
        )
        
        return plausible_strs

    @staticmethod
    def _find_all_from_node(
        node: TrieNode,
        current_word_prefix: str,
        words_discovered: list[str]
    ) -> list[str]:
        """Performs exploration on the Trie from a given node to return all the plausible
        strings that valid from that node."""

        # Exceptional Case: If the node is the end a word
        if node.EOF:
            words_discovered.append(current_word_prefix)

        # Recursive Case: If children still exist from current node
        for child in node.children:
            words_discovered = Trie._find_all_from_node(
                node=node.children[child],
                current_word_prefix=current_word_prefix + child,
                words_discovered=words_discovered
            )

        # Base Case: If no children (reached leaf or backtracking)
        return words_discovered
