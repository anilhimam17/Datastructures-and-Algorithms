class Solution:
    def twoSum_n2(self, nums: list[int], target: int) -> list[int]:
        """Time Complexity O(n^2): Inner and Outer Loop of O(n) * O(n) for computing all the pairs => O(n^2)."""
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if (nums[i] + nums[j]) == target:
                    return [i, j]
        return []
    
    def twoSum_n(self, nums: list[int], target: int) -> list[int]:
        """
        Time Complexity O(n): 
        - Enumeration of Nums O(n).
        - Iterating through Enumeration to fill up seen with non-dup / updated idx of num O(n).
        - If pair found with each search of seen then return O(1)."""
        idx_nums = enumerate(nums)
        seen = {}
        for idx, num in idx_nums:
            diff = target - num
            if diff not in seen:
                seen[num] = idx
            else:
                return [seen[diff], idx]
        return []