class Solution:
    def my_solution_longestConsecutive(self, nums: list[int]) -> int:
        """Reduces a list of unordered integers to a 2D list of consequtive number sequence
        based on the numbers in the list. It then returns the length of the largest consequetive
        number sequence present in the original list."""

        # Sorting the numbers and removing the duplicates
        nums = sorted(list(set(nums)))
        
        # Edge case for singleton list
        if len(nums) == 1:
            return 1

        # Iterating through the list by taking the diff with adjacent elements
        diff_digest = []
        for i in range(1, len(nums)):
            diff = nums[i] - nums[i - 1]
            # If the pair of numbers are consequtive
            if diff in [1, -1]:
                if not diff_digest:
                    diff_digest.append([nums[i-1], nums[i]])
                else:
                    diff_digest[-1].append(nums[i])
            # If the pair of numbers are not consequtive
            else:
                diff_digest.append([nums[i]])

        # Finding the largest consequtive sequence by iterating through the digest for the longest list
        largest_seq_len = 0
        for seq in diff_digest:
            len_seq = len(seq)
            if len_seq > largest_seq_len:
                largest_seq_len = len_seq

        return largest_seq_len

    def slightly_faster_longestConsecutive(self, nums: list[int]) -> int:
        """
        Explanation:
        - Reduces the nums to a non-duplicate set and searches with each number n in nums
        as the starting point the largest consequtive sequence that is possible.
        - For each search number n we almost recursively look for subsequent numbers in the 
        sequence through repeated membership checks while updating a counter.
        - When the while loop exits we compare the largest sequence length so far with the current
        search length to maintain the global maxima which is returned after the search is complete.
        """

        nums_set = set(nums)
        longest = 0

        for n in nums: 
            # skip if not start of a requence 
            # is n-1 in the set? 
            if (n-1) not in nums_set:
                length = 1
                while (n + length) in nums_set:
                    length += 1
                longest = max(length, longest)

        return longest
