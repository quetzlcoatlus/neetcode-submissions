class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Take two strings, check that they're anagrams
        # An anagram is a string with the same characters 
        # but potentially different order

        # s and t consist of lowercase letters, so no need
        # to normalize them

        # Ideas:
        # Dictionary with the count of each letter
        # - O(N) space and time because it traverses each
        #   string once
        # Can brute force but it'll be pretty horrendous
        # Can shortcut if the strings are different lengths

        if len(s) != len(t):
            return False

        char_counts = {}
        # Populate initially with s characters
        for char in s:
            if char not in char_counts:
                char_counts[char] = 1
            else:
                char_counts[char] = char_counts[char] + 1
        
        # Check that the counts for t are the same
        # Could decrement each to 0 in char_counts and
        # validate at the end. Might be a better way.

        for char in t:
            if char not in char_counts:
                return False
            else:
                char_counts[char] = char_counts[char] - 1
        
        for value in char_counts.values():
            if value != 0:
                return False

        return True        
