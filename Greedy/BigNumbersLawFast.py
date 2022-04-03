n,m,k = map(int,input().split())
data = list(map(int,input().split()))

data.sort()
first = data[n-1]
second = data[n-2]

result = 0

count = int(m//(k+1))*k
count += m % (k+1)

result += count*first + int(m//(k+1))*second

print(result)
