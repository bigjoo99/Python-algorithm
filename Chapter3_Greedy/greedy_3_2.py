import sys

input = sys.stdin.readline

N, M, K = map(int, input().split())

array = list(map(int, input().split()))

array.sort()

a = array[-1]       # 첫번쨰로 큰 수
b = array[-2]       # 두번쨰로 큰 수

x = M // (K+1)  
y = M % (K+1)

sum = (a*K + b)*x + a*y

print(sum)