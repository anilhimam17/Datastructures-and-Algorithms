class TrieNode:
    """This class implements the node structure used to build Tries."""

    def __init__(self) -> None:
        self.children: dict[str, TrieNode] = {}
        self.EOF: bool = False
    
    def __str__(self) -> str:
        """Provides a string representation for the Trie Node."""

        return (
            "TrieNode("
            f"children={self.children}, "
            f"EOF={self.EOF}"
            ")"
        )