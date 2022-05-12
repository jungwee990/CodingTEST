array = [7,4,5,8,1,2,3,9,0]

for i in range(1,len(array)):
  for j in range(i,0,-1):
    if array[j] < array[j-1]:
      array[j-1], array[j] = array[j], array[j-1]

    else:
      break

print(array)