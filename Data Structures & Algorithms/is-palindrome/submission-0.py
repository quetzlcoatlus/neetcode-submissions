class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Given a string s
        # Return true if palindrome, otherwise false
        # s characters are constrained, case-insensitive
        # - A-Z, a-z, 0-9
        # Only made of printable ASCII characters
        # Possible edge case with obscure ascii (i.e. space char)

        # Strategies
        # - Brute force: two passes save copy O(n), O(n)
        # - Two Pointer: one pass O(n), O(1)

        # No chance sorting matters (worse than brute force)
        # No chance additional data structure helps (also worse than bf)

        # Brute force solution
        char_arr = []
        for c in s.lower():
            if c.isalnum():
                char_arr.append(c)
        print(char_arr)
        i = 0
        for c in s.lower()[::-1]:
            if c.isalnum():
                if c != char_arr[i]:
                    return False
                i += 1
        return True

