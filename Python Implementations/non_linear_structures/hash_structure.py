from collections.abc import Callable
from typing import Any

from non_linear_structures.hash_utils import COLLISION_RESOLUTION_MAP
from linear_structures.sll import SLL


class Hash:
    """This class implements a Hashmap Datastructure comprising all of its properties
    and methods for storing and searching data."""

    # ==== Standard Methods ====
    def __init__(
            self,
            hash_function: Callable[[Any], int] = hash,
            collision_resolution_technique: str = "Direct Chaining",
            table_size: int = 10
        ) -> None:

        # Providing the Hash Function by Reference
        self.hash_function = hash_function
        
        # Resolving the Collision Resolution Technique
        try:
            self.collision_resolution_method = Hash._get_collision_method(
                method_name=collision_resolution_technique
            )
        except ValueError:
            print("The Collision Resolution Method provided was invalid defaulting to Direct Chaining.")
            self.collision_resolution_method = COLLISION_RESOLUTION_MAP["Direct Chaining"]
        
        self.table_size = table_size
        
        # Creating a Hash Table of Linked Lists
        if collision_resolution_technique == "Direct Chaining":
            self.hash_table = [SLL() for _ in range(self.table_size)]
        # Creating a Hash Table of Empty Tuples
        else:
            self.hash_table = [(None, None) for _ in range(self.table_size)]

    def __str__(self) -> str:
        """Provides a string representation for the Hash Structure."""

        hash_table_str = ""
        for i in range(self.table_size):
            hash_table_str += str(self.hash_table[i]) + "\n"

        return hash_table_str

    # ==== Helper Functions ====
    @staticmethod
    def _get_collision_method(method_name: str) -> Callable:
        """Validates the Collision Resolution Method passed during Initialisation."""

        # If collision method valid
        if method_name in COLLISION_RESOLUTION_MAP:
            return COLLISION_RESOLUTION_MAP[method_name]
        
        # If collision method invalid
        raise ValueError
    
    def _get_index(self, hash_value: int) -> int:
        """Calculates the Hash Table index from the Hash Value."""

        return hash_value % self.table_size
    
    # ==== Member Methods ====
    def insert(self, key: Any, value: Any) -> None:
        """Inserts any value into the Hash Table by calculating the Hash Value."""

        # Generates the Hash Value
        hash_value_raw = hash(key)

        # Calculates the Hash Table Index
        hash_index = self._get_index(hash_value_raw)
        
        # Logging the State to view the Collision Handling
        print(f"Digest Value: {hash_value_raw}, Hash Index: {hash_index}")
        
        # Inserting the Value into the Hash Table
        self.collision_resolution_method(
            hash_index=hash_index,
            key_to_insert=key,
            value_to_insert=value,
            hash_table=self.hash_table
        )
