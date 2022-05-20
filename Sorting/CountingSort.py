array = [8,8,7,6,6,6,9,0,3,4,1,2,5]
count = [0] * (max(array) + 1)
for i in range(len(array)):
  count[array[i]] += 1

for i in range(len(count)):
  for j in range(count[i]):
    print(i, end = '')
  