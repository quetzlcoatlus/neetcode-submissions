class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Given strings s and t
        # Return true if two are anagrams
        # Constraints: already lowercase and English

        # An anagram is a string that contains the same characters

        # Hashmap character counts (only 26 letters) so O(1)
        # Could also sort each string and check each letter

        # Sorting Approach
        # if len(s) != len(t):
        #     return False

        # sorted_s = sorted(s)
        # sorted_t = sorted(t)
        # for i in range(len(s)):
        #     if sorted_s[i] != sorted_t[i]:
        #         return False
        # return True

        # Hashmap Approach (more optimal)
        if len(s) != len(t):
            return False

        # Populate with counts of either
        s_chars = {}
        for char in s:
            if char not in s_chars:
                s_chars[char] = 1
            else:
                s_chars[char] = s_chars[char] + 1
        for char in t:
            if char not in s_chars:
                return False
            else:
                s_chars[char] = s_chars[char] - 1
        # Check that all letters are 0
        for value in s_chars.values():
            if value != 0:
                return False
        return True