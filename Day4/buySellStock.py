'''You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
'''
# O(n*n)
# def stockProfit(prices):
#     isThereProfit=False
#     for i in range(len(prices)-1):
#         if(prices[i]<prices[i+1]):
#             isThereProfit=True
#             break
#     if(isThereProfit):
#         # find best profit
#         currentProfit=0
#         maximumProfit=0
#         for i in range(len(prices)-1):
#             for j in range(i,len(prices)):
#                 currentProfit=-(prices[i]-prices[j])
#                 if(currentProfit>maximumProfit):
#                     maximumProfit=currentProfit
#                 currentProfit=0
#         return maximumProfit


#     else:
#         return 0

# O(n)

def stockProfit(prices):
    left=0
    right=1
    maximumProfit=0
    while(right<len(prices)):
        if(prices[left]<prices[right]):
            profit=prices[right]-prices[left]
            maximumProfit=max(profit,maximumProfit)
        else:
            left=right
        right+=1
    return maximumProfit
        

# driver code
prices1 = [7,2,5,1,2,4]
prices2 = [7,6,4,3,1]
print(stockProfit(prices1))


