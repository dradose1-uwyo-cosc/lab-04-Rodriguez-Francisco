items= ['eggs','Milk','coffee','beef','chicken']
prices = [3,4,5,10,6]
for i in range(len(items)):
    print(f"I bought {items[i]} for {prices[i]}")
total=0 
for i in (prices):
    total += i
print(f"I spent {total} at walmart")

cheap = min(prices)
cindex = prices.index(cheap)

expensive = max(prices)
eindex= prices.index(expensive)

print(f"The most expensive was {items[eindex]}")
print(f"The cheapest was {items[cindex]}")