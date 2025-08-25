# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different 
# day in the future to sell that stock.
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

def maxProfit(prices: list[int]) -> int: #Compexity O(N) not bad, not good
    todayProfit = float("inf")
    bestProfit = -float("inf")
    for i in range(len(prices)):
        if prices[i] < todayProfit:
            todayProfit = prices[i]
        totalProfit = prices[i] - todayProfit
        if(bestProfit < totalProfit):
            bestProfit = totalProfit
    return bestProfit

#This solution is good (i would, i make it in 20 min), but the complexity is shit, whith large arrays we have Time Limit Exceeded 
    # bestPrice = 0
    # for i in range(len(prices)):
    #     for j in range(i + 1, len(prices)):
    #         if prices[i] < prices[j] and (prices[j] - prices[i]) > bestPrice:
    #             bestPrice = prices[j] - prices[i]
    # return bestPrice


newPrices = [7,1,5,3,6,4]
za = input()
print(maxProfit(newPrices))