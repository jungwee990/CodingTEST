# array = [2,4,6,8,0,1,3,5,7,9]

# def quick_sort(array,start,end):
#   if start >= end:
#     return

#   left = start + 1
#   right = end
#   pivot = start
#   while left <= right:
#     while left <= end and array[left] < array[pivot]:
#       left += 1

#     while right > start and array[right] > array[pivot]:
#       right -= 1

#     if left < right: #엇갈리지 않은경우
#       array[left],array[right] = array[right], array[left]

#     else: #엇갈린 경우
#       array[pivot],array[right] = array[right], array[pivot]

#   quick_sort(array, start, right-1)
#   quick_sort(array, right + 1, end)

# quick_sort(array,0,len(array)-1)   
# print(array)

# 다른풀이, 파이썬에서만 사용가능함 
array = [2,4,6,8,0,1,3,5,7,9]

def quick_sort(array):
  if len(array) <= 1:
    return array

  pibot = array[0]
  tail = array[1:]

  left = [x for x in tail if x <= pibot]
  right = [x for x in tail if x > pibot]

  return quick_sort(left) + [pibot] + quick_sort(right)

print(quick_sort(array))

  