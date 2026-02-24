from typing import Any

from linear_structures.sll import SLL


# ==== Collision Resolution Methods ====
def direct_chaining(
        hash_index: int,
        key_to_insert: Any,
        value_to_insert: Any,
        hash_table: list[SLL]
    ) -> None:
    """Applies the Direct Chaining Method to resolve a collision that 
    has occurred during Hashing."""

    # Chaining in the key, value
    hash_table[hash_index].append(value=(key_to_insert, value_to_insert))

def linear_probing(
        hash_index: int,
        key_to_insert: Any,
        value_to_insert: Any,
        hash_table: list[tuple[Any, Any]]
    ) -> None:
    """Applies the Linear Probing Method to resolve a collision that 
    has occurred during Hashing."""
    
    table_len = len(hash_table)
    current_index = hash_index

    # If hash index is not empty, traverse linearly to find the next free location
    for _ in range(table_len):
        if hash_table[current_index] == (None, None):
            hash_table[current_index] = (key_to_insert, value_to_insert)
            return
        current_index = (current_index + 1) % table_len
    raise OverflowError

def quadratic_probing(
        hash_index: int,
        key_to_insert: Any,
        value_to_insert: Any,
        hash_table: list[tuple[Any, Any]]
    ) -> None:
    """Applies the Quadratic Probing Method to resolve a collision that 
    has occurred during Hashing."""

    table_len = len(hash_table)
    current_index = hash_index

    # If hash index is not empty, traverse quadratically to find the next free location
    for i in range(table_len):
        if hash_table[current_index] == (None, None):
            hash_table[current_index] = (key_to_insert, value_to_insert)
            return
        current_index = (hash_index + int(i ** 2)) % table_len
    raise OverflowError


# ==== Mapping the Functions ====
COLLISION_RESOLUTION_MAP = {
    "Direct Chaining": direct_chaining,
    "Linear Probing": linear_probing,
    "Quadratic Probing": quadratic_probing,
}