a,b = map(int, input().split())

c = [False,False] + [True]*(b-1)

primes=[]

for i in range(2,b+1):
  if c[i]:
      for j in range(2*i, b+1, i):
            c[j] = False
      if i<a:
         continue
      primes.append(i)
    
for i in primes:
    print(i) 
    