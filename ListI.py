hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]
prices = [30, 25, 40, 20, 20, 35, 50, 35]
last_week = [2, 3, 5, 8, 4, 4, 6, 2]

total_price = 0

for price in range(0,len(prices)):
  total_price=total_price+prices[price]

print(total_price)

avg_price = total_price/2

print(avg_price)

new_prices = [price-5 for price in prices]

print(new_prices)

total_revenue = 0

for i in range(0,len(hairstyles)):
  total_revenue=total_revenue+prices[i]*last_week[i]

print("Total revenue " + str(total_revenue) + "!")

avg_total_revenue = total_revenue/7

cuts_under_30 = [hairstyles[i] for i in range(0,len(new_prices)) if new_prices[i] < 30]

print("These cuts are under 30$ " + cuts_under_30 + "!")

