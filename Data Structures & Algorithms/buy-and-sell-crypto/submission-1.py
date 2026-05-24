class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # buy low sell high
        # brute force is too slow O(n^2) roughly

        # Cases
            # 10, 1, 5, 6, 7, 1
            # 10, 8, 7, 5, 2
            # empty
            # 5

        # sliding window
        # left and right pointer
        # - left to local min
        # - right to local max

        # initialize left and right
        # push right forward
        # if right is > left, left = right
        # regardless right continues

        # One pass O(N) time
        # Static variables (4) so O(1) space
        if len(prices) <= 1:
            return 0

        max_profit = 0
        l, r = 0, 1

        while r < len(prices):
            profit = prices[r] - prices[l]
            if profit > max_profit:
                max_profit = profit
            if prices[r] < prices[l]:
                l = r
            r += 1

        return max_profit
