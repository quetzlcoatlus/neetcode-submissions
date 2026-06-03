class Solution:
    def isValid(self, s: str) -> bool:
        # Input: str with ()[]{}
        # Output: boolean isValid
        # Edges: len(s) == 1
        # Constraints: len(s) >= 1; <= 1000
        # Test Cases:
        # - "([{}])"    T
        # - "[(])"      F
        # - "["         F
        # - "}{}"       F
        # - "[]{()}"    T
        # Questions:
        # - 

        # Stack: HIGH
        # Array/List: MED

        # Strategies:
        # - Adding new open parentheses is fine.
        # Char dictionary to associate opening with closing parentheses
        # if we add a closing parentheses, check the top of the stack
        # if the top is the corresponding opening character, pop and continue
        # if the top is not the corresponding opening character, return False
        # if we make it through s, return whether the stack is empty
        # - Treat string like array, do a pass with pointers checking previous

        # Happy path case: s = "([{}])"
        # st = 
        # i.
        # 0. opening, push
        # 1. opening, push
        # 2. opening, push
        # 3. closing, check top, is opening, pop, continue
        # 4. closing, check top, is opening, pop, continue
        # 5. closing, check top, is opening, pop, continue
        # Exit loop, st is empty, return True

        # Edge case: s = "}{}"
        # st = 
        # i.
        # 0. closing, check top, is not opening, return false

        # Edge case: s = "["
        # st = 
        # i. 
        # 0. opening, push
        # Exit loop, st not empty, return False

        st = []
        paren_map = {
            ')': '(',
            ']': '[',
            '}': '{',
        }
        for c in s:
            # character is opening
            if c not in paren_map:
                st.append(c)
            # character is closing
            else:
                if len(st) == 0 or paren_map[c] != st.pop():
                    return False
        return len(st) == 0



