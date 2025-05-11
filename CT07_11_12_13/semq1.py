daily_sales = [1205, 986, 1354, 10535, 15741, 11200, 800, 
               13056, 952, 1100, 1025, 8574, 14014, 9987, 
               1238, 1458, 7803, 900, 13674, 14539, 13241, 
               10886, 7541, 8743, 1482, 11523, 977, 12181, 
               8903, 1008, 1530]

max_sales = max(daily_sales)
max_day = daily_sales.index(max_sales) + 1

min_sales = min(daily_sales)
min_day = daily_sales.index(min_sales) + 1

ave_sales = round(sum(daily_sales) / len(daily_sales), 2)


print(f"{max_day} August has the highest sales of ${max_sales}")
print(f"{min_day} August has the highest sales of ${min_sales}")
print(f"Average daily sales for August is ${ave_sales}")



