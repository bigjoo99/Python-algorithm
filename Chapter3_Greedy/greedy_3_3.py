import sys

input = sys.stdin.readline

N, M = map(int, input().split())
arr_min = []

for i in range(N):
    array = list(map(int, input().split()))
    minimum = min(array)
    arr_min.append(int(minimum))
    
print(max(arr_min))
