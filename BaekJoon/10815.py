N = int(input())

arr_n = list(map(int, input().split()))

M = int(input())

arr_m = list(map(int,input().split()))

result = []

for i in arr_m:
    if i in arr_n:
        result.append(1)
    else:
        result.append(0)
        
for i in result:
    print(i, end=' ')