from collections import Counter

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        
        # Counting the no of occurrences of the elements in the iterable
        count_elements = Counter(nums)

        # Sorting the count for returning top k
        sorted_count = tuple(sorted(
            count_elements.items(),
            key=lambda x: x[-1],
            reverse=True
        ))

        return [i for i, _ in sorted_count[:k]]