n = int(1260)

count = 0

coin_array = [500, 100, 50, 10]

for coin in coin_array:
    count += n // coin
    n = n%coin
    
print(count)