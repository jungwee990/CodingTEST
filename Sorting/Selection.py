array = [7,6,5,9,0,1,3,2,4,8]

for i in range(len(array)):
  min = i
  for j in range(i+1,len(array)):
    if array[min] > array[j]:
      array[min],array[j] = array[j],array[min]

print(array)