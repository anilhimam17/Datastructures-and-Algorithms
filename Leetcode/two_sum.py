class Solution:
    def twoSum_n2(self, nums: list[int], target: int) -> list[int]:
        """Time Complexity O(n^2): Inner and Outer Loop of O(n) * O(n) for computing all the pairs => O(n^2)."""
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if (nums[i] + nums[j]) == target:
                    return [i, j]
        return []