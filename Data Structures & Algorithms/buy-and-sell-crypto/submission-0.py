class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Given int array 'prices'
        # prices[i] is price of NeetCoin on the ith day
        # Choose a single day to buy and different one after to sell
        # Return maximum profit possible, minimum 0

        # Buy low, sell high
        # Calculation of difference between days is useful
        # Potential for sorting if we keep track of original idx
        # Potential to go backwards through the array

        # Strategies
        # - Brute force, check all possibilities and save max O(n^2), O(1)
        # - Backwards, find maximum value past the current (same as bf)
        # - Sorting and save idx, find max sell/buy day and traverse O(n^2) worst O(n)
        # - Sliding window, 2 pointers, buy and sell
        #   - buy updates to sell on new minimum, sell updates each time
        #   - exit loop when sell == len(prices) and return max

        # Sliding window approach
        buy = sell = 0
        max_profit = 0
        while (sell < len(prices)):
            curr_profit = prices[sell] - prices[buy]
            if curr_profit > max_profit:
                max_profit = curr_profit
            
            if prices[sell] < prices[buy]:
                buy = sell
            sell += 1
        return max_profit