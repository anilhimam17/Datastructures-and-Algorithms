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
        # Double sized for Quadratic due larger quadratically growing indexes
        elif collision_resolution_technique == "Quadratic Probing":
            self.hash_table = [(None, None) for _ in range(self.table_size)]
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
    def _get_collision_method(method_name: str) -> Callable[[int, Any, Any, list], None]:
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
        print(f"Digest Value: {hash_value_raw}, Initial Hash Index: {hash_index}")
        
        # Inserting the Value into the Hash Table
        try:
            self.collision_resolution_method(
                hash_index,
                key,
                value,
                self.hash_table
            )
        except OverflowError:
            print("The Hash Table is currently full extending the table to insert the value.")
            
            # Increasing the size by multiple of 2
            self.table_size *= 2

            # Copying over the key value pairs from the old hash table
            new_hash_table = [(None, None) for _ in range(self.table_size)]

            # Recalculating the Hash Digest for each of the Key Value pairs
            for k, v in self.hash_table:
                
                # Skipping the None pairs
                if k is None:
                    continue  
           
                re_calc_raw_hash_value = self.hash_function(k)
                re_calc_hash_index = self._get_index(hash_value=re_calc_raw_hash_value)
                self.collision_resolution_method(
                    re_calc_hash_index,
                    k,
                    v,
                    new_hash_table
                )

            # Updating the Instance-Level Hash Table and Size
            self.hash_table = new_hash_table

            # Retrying the insertion
            new_hash_index = self._get_index(self.hash_function(key))
            self.collision_resolution_method(
                new_hash_index,
                key,
                value,
                self.hash_table
            )

    def __getitem__(self, key: Any) -> Any:
        """Performs the access operation to access the stored values in the Hash Structure."""

        # Calculating the raw hash value
        hash_value_raw = self.hash_function(key)

        # Calculating the hash index
        hash_index = self._get_index(hash_value=hash_value_raw)

        # If Direct Chaning is being used
        if self.collision_resolution_method == COLLISION_RESOLUTION_MAP["Direct Chaining"]:
            
            # Accessing the SLL
            hash_bucket = self.hash_table[hash_index]
            assert isinstance(hash_bucket, SLL), "Hash Bucket in Direct Chaining has to be a LL."
            
            # Traversing the SLL till the right Key, Value pair is found
            for node in hash_bucket:
                k, v = node.value
                if k == key:
                    return v
            raise KeyError("The given key was not found in the Hash Structure")
        # If Open Addressing is being used
        # Linear Probing
        # elif self.collision_resolution_method == COLLISION_RESOLUTION_MAP["Linear Probing"]:

