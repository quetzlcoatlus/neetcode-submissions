class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Given strings s and t
        # Return true if two are anagrams
        # Constraints: already lowercase and English

        # An anagram is a string that contains the same characters

        # Hashmap character counts (only 26 letters) so O(1)
        # Could also sort each string and check each letter

        # Sorting Approach
        if len(s) != len(t):
            return False

        sorted_s = sorted(s)
        sorted_t = sorted(t)
        for i in range(len(s)):
            if sorted_s[i] != sorted_t[i]:
                return False
        return True