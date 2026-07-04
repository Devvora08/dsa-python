# best time to buy sell stocks

def best_buy(num):
    max_pro = 0
    min_price = num[0]

    for i in range(1,len(num)):
        curr_best = 0
        if num[i] > min(num[i-1], min_price):
            curr_best = num[i] - min(num[i-1], min_price)
            max_pro = max(max_pro, curr_best)
        
        min_price = min(min_price, num[i])
    
    return max_pro
