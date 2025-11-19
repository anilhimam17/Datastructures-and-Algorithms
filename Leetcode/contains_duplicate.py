from collections import defaultdict


class Solution:
    def containsDuplicate_n2(self, nums: list[int]) -> bool:
        """Time Complexity O(n^2): Outer loop O(n) + Innate Inner loop [not in check] O(n)."""
        non_dup_nums = []
        for num in nums:
            if num not in non_dup_nums:
                non_dup_nums.append(num)
            else:
                return True
        else:
            return False

    def containsDuplicate_n(self, nums: list[int]) -> bool:
        """Time Complexity O(n): Outer loop O(n) + Key checks direct hash location O(1)."""
        lookup_table = defaultdict(int)
        for num in nums:
            if not lookup_table[num]:
                lookup_table[num] += 1
            else:
                return True
        else:
            return False
        
    def containsDuplicate_n_faster(self, nums: list[int]) -> bool:
        """
        Time Complexity O(n): Outer loop O(n) + Checks [in using hash - set => hash set] direct location O(1).
        Faster than defaultdict due to no key-val pairs.
        """
        non_dup_set = set()
        for num in nums:
            if num in non_dup_set:
                return True
            else:
                non_dup_set.add(num)
        return False