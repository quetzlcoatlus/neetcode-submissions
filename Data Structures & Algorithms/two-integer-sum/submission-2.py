class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Given array nums and target int
        # Return i and j such that the nums add to target
        # Exactly one solution exists
        # Return smaller index first

        # Strategies
        # - Brute force O(n^2), O(1)
        # - Sorting and keeping track O(nlogn) + O(n)
        # - Hashmap one and two pass O(n) + O(n)

        # One pass hashmap solution
        # Check if complement exists in hm
        # If it doesn't, continue and add value with index
        # If it does, get return index of both, hm one is smaller

        hm = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in hm:
                return [hm[complement], i]
            hm[num] = i
        return []