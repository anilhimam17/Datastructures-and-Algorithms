from typing import Any


class AVLNode:
    """Implements the node structure used to construct AVL Trees."""

    # ==== Standard Methods ====
    def __init__(self, value: Any) -> None:
        
        self.value: Any = value
        self.left_child: AVLNode | None = None
        self.right_child: AVLNode | None = None
        self.height = 1

    def __str__(self) -> str:
        """Provides a string representation for the AVLNode."""
        
        return f"AVLNode(value={self.value}, height={self.height})"
