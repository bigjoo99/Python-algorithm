n = int(input())
arr = set(map(int,input().split()))
m = int(input())
arr1 = list(map(int,input().split()))

for num in arr1:
    print(1) if num in arr else print(0)