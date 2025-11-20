from collections import Counter, defaultdict


class Solution:
    def groupAnagrams_nm(self, strs: list[str]) -> list[list[str]]:
        """
        Time Complexity O(n . m):
        - O(n) for n list of n strings in strs we iterate for anagram groups.
        - O(m) for each string
            -> Create a counter instance O(m).
            -> Max string length of m.
            -> Max dictionary size initialised by the counter k <= 26.
        -> Sorting: O(1) ~ O(k log k) for 26 chars it reduces to O(1).
        -> Values Generation: O(n) since we create a shallow copy of n strings.
        """
        pairs = defaultdict(list)
        for string in strs:
            count_string = tuple(sorted(Counter(string).items()))
            pairs[count_string].append(string)
        return list(pairs.values())
    
    def groupAnagrams_n_times_mlogm(self, strs: list[str]) -> list[list[str]]:
        """
        Time Complexity O(n . m):
        - O(n) for n list of n strings in strs we iterate for anagram groups.
        - O(m log m) ~ O(m) for each string
            -> Sorted chars of string O(m log m) ~ O(m) as m <= 100.
            -> tuple construction O(m) scaling with size.
        -> Values Generation: O(n) since we create a shallow copy of n strings.
        
        While time complexity is asymptootically the same as the baseline there are fewer ops
        due to the removal of Counter.
        """
        pairs = defaultdict(list)
        for string in strs:
            sort_string = tuple(sorted(string))
            pairs[sort_string].append(string)
        return list(pairs.values())
    
