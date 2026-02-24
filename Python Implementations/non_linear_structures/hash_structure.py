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
        elif collision_resolution_technique == "Quadratic Probing":
            # Double sized for Quadratic due larger quadratically growing indexes
            self.table_size *= 2
            self.hash_table = [(None, None) for _ in range(self.table_size)]
        else:
            self.hash_table = [(None, None) for _ in range(self.table_size)]

    def __str__(self) -> str:
        """Provides a string representation for the Hash Structure."""

        hash_table_str = [str(self.hash_table[i]) for i in range(self.table_size)]
        return "\n".join(hash_table_str)
    
    def __len__(self) -> int:
        """Provides the no of non-null elements present in the Hash Structure."""

        # If Direct Chaining is being used
        if isinstance(self.hash_table[0], SLL):
            count = sum(
                [
                    self.hash_table[i].no_of_elements  # type: ignore
                    for i in range(self.table_size)
                ]
            ) 
            return count
        # If Open Addressing is being used
        count = sum([1 if self.hash_table[i] != (None, None) else 0 for i in range(self.table_size)])
        return count
    
    @property
    def load_factor(self) -> float:
        """Provides the Number of Elements to Hash Table ratio to improve downstream
        efficiency of the Hash Structure."""

        return len(self) / self.table_size

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
    
    def _resize_hash_table_sll(self) -> None:
        """Resizes the Hash Table using Direct Chaining for better operational efficiency."""

        # New Hash Table to copy the elements
        new_hash_table = [SLL() for _ in range(self.table_size)]
        for hash_bucket in self.hash_table:
            assert isinstance(hash_bucket, SLL), "Hash Bucket in Direct Chaining has to be an LL."

            # Skipping Null Entries
            if hash_bucket.head is None:
                continue
            
            # Traversing the elements of the Hash Bucket for new insertion
            for node in hash_bucket:
                key, value = node.value
                initial_hash_index = self._get_index(hash_value=self.hash_function(key))
                self.collision_resolution_method(
                    initial_hash_index,
                    key,
                    value,
                    new_hash_table
                )

        # Updating the Instance-Level Hash Table to the newly resized Hash Table
        self.hash_table = new_hash_table

    def _resize_hash_table_tuple(self) -> None:
        """Resizes the Hash Table using Open Addressing for better operational efficiency."""

        # New Hash Table to copy the elements
        new_hash_table = [(None, None) for _ in range(self.table_size)]
        
        # Traversing the Hash Table for new insertion
        for hash_bucket in self.hash_table:
            assert isinstance(hash_bucket, tuple), "Hash Bucket in Open Addressing has to be an Tuple."

            # Skipping Null Entries
            if hash_bucket == (None, None):
                continue
            
            key, value = hash_bucket
            intial_hash_index = self._get_index(hash_value=self.hash_function(key))
            self.collision_resolution_method(
                intial_hash_index,
                key,
                value,
                new_hash_table
            )

        # Updating the Instance-Level Hash Table to the newly resized Hash Table
        self.hash_table = new_hash_table
    
    # ==== Member Methods ====
    def insert(self, key: Any, value: Any) -> None:
        """Inserts any value into the Hash Table by calculating the Hash Value."""
        
        # Resizing the Hash Table proactively to improve efficiency
        if self.load_factor >= 0.7:
            print("Resizing the Hash Table since the Load Factor condition was triggered.")

            # Increasing Table Size
            self.table_size *= 2

            # If Direct Chaining is being used
            if isinstance(self.hash_table[0], SLL):
                self._resize_hash_table_sll()
            # If Open Addressing is being used
            else:
                self._resize_hash_table_tuple()

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
            
            # Resizing the Hash Tables on Overflow
            if isinstance(self.hash_table[0], SLL):
                self._resize_hash_table_sll()
            else:
                self._resize_hash_table_tuple()

            # Retrying the Insertion
            new_intial_hash_index = self._get_index(hash_value=self.hash_function(key))
            self.collision_resolution_method(
                new_intial_hash_index,
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
        # Accessing the Initial Hash Index to check K, V pair
        hash_bucket = self.hash_table[hash_index]
        assert isinstance(hash_bucket, tuple), "Hash Bucket in Open Addressing has to be a Tuple."

        # Linear Probing
        if self.collision_resolution_method == COLLISION_RESOLUTION_MAP["Linear Probing"]:
            # If initial index holds the correct key
            if hash_bucket[0] == key:
                return hash_bucket[1]
            # Carry out linear probing to find the correct key
            else:
                current_index = hash_index
                
                for _ in range(self.table_size):
                    current_index = (current_index + 1) % self.table_size
                    hash_bucket = self.hash_table[current_index]
                    assert isinstance(hash_bucket, tuple), "Hash Bucket in Open Addressing has to be a Tuple."

                    if hash_bucket[0] == key:
                        return hash_bucket[1]
                
                raise KeyError("The given key was not found in the Hash Structure")
        # Quadratic Probing
        else:
            # If initial index holds the correct key
            if hash_bucket[0] == key:
                return hash_bucket[1]
            # Carry out quadratic probing to find the correct key
            else:
                current_index = hash_index
                
                for i in range(self.table_size):
                    current_index = (hash_index + int(i ** 2)) % self.table_size
                    hash_bucket = self.hash_table[current_index]
                    assert isinstance(hash_bucket, tuple), "Hash Bucket in Open Addressing has to be a Tuple."

                    if hash_bucket[0] == key:
                        return hash_bucket[1]
                
                raise KeyError("The given key was not found in the Hash Structure")
