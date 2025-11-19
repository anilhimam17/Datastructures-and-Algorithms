from collections import Counter


class Solution:
    """
    Time Complexity O(N): 
    - Counter Construction for each k char string is O(k >> N).
    - Comparison is O(1) since at worst case the dict has 26 key-val pairs for iteration during comparison.
    - Return O(1).
    """
    def isAnagram(self, s: str, t: str) -> bool:
            return Counter(s) == Counter(t)