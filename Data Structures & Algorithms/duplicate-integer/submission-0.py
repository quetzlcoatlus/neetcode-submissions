class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Given integer array nums
        # Return true if any value appears more than once
        # Return false if no values appear more than once

        # Ideas:
        # Create a set, check against set
        # - Drawback is that it is O(N) space
        # Sort beforehand and check neighbors
        # - Drawback is that it is O(NlogN) time

        # Set idea seems better overall
        unique_nums = set()
        for num in nums:
            if num in unique_nums:
                return True
            # Add unique numbers to set
            unique_nums.add(num)
        return False