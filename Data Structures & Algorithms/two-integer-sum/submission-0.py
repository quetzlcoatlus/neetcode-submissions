class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Given array nums and int target
        # Return earliest i and j such that:
        # - nums[i] + nums[j] == target and i != j
        # Constraints: every input has exactly one valid solution
        # Nums can be negative and so can the target
        # Nums is not sorted

        # Trivial O(n^2) approach where we check every j after i
        # Hashmap? 
        # Sorted left and right pointer O(nlogn), O(n) space
        # - If the target is larger than left + right:
        #   - Then we increment left
        # - If the target is smaller than left + right:
        #   - Then we decrement right
        # - Exit if left == right

        A = []
        # Retains initial indices
        for i, num in enumerate(nums):
            A.append([num, i])

        left, right = 0, len(nums) - 1
        A.sort()
        # Sorting requires we retain the original indices
        while left < right:
            curr = A[left][0] + A[right][0]
            if curr == target:
                # first idx needs to be lower
                return [min(A[left][1], A[right][1]),
                        max(A[left][1], A[right][1])]
            elif curr < target:
                left += 1
            else: # curr > target
                right -= 1
        return []
