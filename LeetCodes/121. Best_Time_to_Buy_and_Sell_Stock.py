# You are given an array prices where prices[i] is the price of a given stock on the ith day.

# You want to maximize your profit by choosing a single day to buy one stock and choosing a 
# different day in the future to sell that stock.

# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

def max_profit(prices: list[int]) -> int:
    # no_stock = 0
    # hold_stock = -prices[0]

    # for i in range(1, len(prices)):
    #     prev_ns = max(no_stock, hold_stock + prices[i])
    #     prev_hs = max(hold_stock, no_stock - prices[i])
    #     no_stock = prev_ns
    #     hold_stock = prev_hs
    # return no_stock

    profit = 0
        
    for i in range(1, len(prices)):
        if prices[i] > prices[i-1]:
            profit += prices[i] - prices[i-1]
    
    return profit

    # min_p = float('inf')
    # max_p = 0
    # dp = [0] * len(prices)

    # for p in prices:
    #     if p < min_p:
    #         min_p = p
    #     elif p - min_p > max_p:
    #         max_p = p - min_p

    # return int(max_p)

prices = [7,1,5,3,6,4]
input()
print(max_profit(prices=prices))

#hell nah i've really improve my leetcode skills 
# def maxProfit(prices: list[int]) -> int: #Compexity O(N) not bad, not good
#     todayProfit = float("inf")
#     bestProfit = -float("inf")
#     for i in range(len(prices)):
#         if prices[i] < todayProfit:
#             todayProfit = prices[i]
#         totalProfit = prices[i] - todayProfit
#         if(bestProfit < totalProfit):
#             bestProfit = totalProfit
#     return bestProfit

#This solution is good (i would, i make it in 20 min), but the complexity is shit, whith large arrays we have Time Limit Exceeded 
    # bestPrice = 0
    # for i in range(len(prices)):
    #     for j in range(i + 1, len(prices)):
    #         if prices[i] < prices[j] and (prices[j] - prices[i]) > bestPrice:
    #             bestPrice = prices[j] - prices[i]
    # return bestPrice