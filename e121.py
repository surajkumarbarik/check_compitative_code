# def maxProfit(prices):  #this minimum checking and profit calculation will be occure for each elements looping - pending
    # if len(prices):
    #     min_el = min(prices)
    #     max_el_after_min = max(prices[prices.index(min_el):])
    #     profit =  max_el_after_min - min_el
    #     print(prices[:prices.index(min_el)])
    #     for i in range(len(prices)-1):
    #         if len(prices[:prices.index(min_el)]):
    #             max_el_before_1st_min = max(prices[:prices.index(min_el)])
    #             min_el_before_1st_min = min(prices[:prices.index(min_el)])
    #             return (max_el_before_1st_min-min_el_before_1st_min) if (max_el_before_1st_min-min_el_before_1st_min) > profit and prices.index(max_el_before_1st_min)>prices.index(min_el_before_1st_min) else profit
    #         else:
    #             return profit
    # else:
    #     return 0

def maxProfit(prices):
    profit = 0
    if len(prices):
        min_el = min(prices)
        while min_el != "x" and len(prices[:prices.index(min_el)+1]):
            max_el_after_min = max(prices[prices.index(min_el):])
            # print(prices[prices.index(min_el):])
            # print(prices[prices.index(min_el):].index(max_el_after_min))
            # print(prices.index(min_el))
            print(min_el, max_el_after_min)
            profit = (max_el_after_min- min_el) if (max_el_after_min-min_el) > profit else profit
            min_el = min(prices[:prices.index(min_el)]) if len(prices[:prices.index(min_el)]) else "x"
        return profit

prices = [1,2,1,5,3,6,4]
print(maxProfit(prices))