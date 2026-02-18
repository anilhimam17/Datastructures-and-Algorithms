class TrieNode:
    """This class implements the node structure used to build Tries."""

    def __init__(self, value: str) -> None:
        self.value: list[str] = [value]
        self.children: dict[str, TrieNode] = {}
        self.EOF: bool = False
    
    def __str__(self) -> str:
        """Provides a string representation for the Trie Node."""

        return (
            "TrieNode(\n"
            f"value={self.value}\n"
            f"EOF={self.EOF}\n"
            f"children={self.children}\n)"
        )