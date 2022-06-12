# 피보나치수열 재귀적구현

# d = [0] * 101
# def fibo(x):
#   if x==1 or x==2: 
#     return 1

#   if d[x] != 0:
#     return d[x]

#   d[x] = fibo(x-1) + fibo(x-2)
#   return d[x]

# print(fibo(100))

# # 프린트출력
# d = [0] * 100
# def fibo(x):
#   print('f(' + str(x) + ')', end= ' ')
#   if x==1 or x==2: 
#     return 1
#   #print('f(' + str(x) + ')', end= ' ')
#   if d[x] != 0:
#     return d[x]

#   d[x] = fibo(x-1) + fibo(x-2)
#   return d[x]

# fibo(6)

# 보텀업방식
d = [0] * 100

d[1] = 1
d[2] = 1
n = 99

for i in range(3, n+1):
  d[i] = d[i-1] + d[i-2]

print(d[n])