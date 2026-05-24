class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Given a string s
        # Return true if palindrome, otherwise false
        # s characters are constrained, case-insensitive
        # - A-Z, a-z, 0-9
        # Only made of printable ASCII characters
        # Possible edge case with obscure ascii (i.e. space char)

        # Strategies
        # - Reverse String: save copy O(n), O(n)
        # - Two Pointer: one pass O(n), O(1)

        # No chance sorting matters (worse than brute force)
        # No chance additional data structure helps (also worse than bf)

        # Brute force solution
        # char_arr = []
        # for c in s.lower():
        #     if c.isalnum():
        #         char_arr.append(c)
        # print(char_arr)
        # i = 0
        # for c in s.lower()[::-1]:
        #     if c.isalnum():
        #         if c != char_arr[i]:
        #             return False
        #         i += 1
        # return True

        # Simpler brute force solution
        # new_str = ''
        # for c in s:
        #     if c.isalnum():
        #         new_str += c.lower()
        # return new_str == new_str[::-1]

        # Left and right pointer solution
        left, right = 0, len(s) - 1
        while (left < right):
            if not s[left].isalnum():
                left += 1
                continue
            elif not s[right].isalnum():
                right -= 1
                continue
            
            # Both are valid alphanumeric characters now
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True
