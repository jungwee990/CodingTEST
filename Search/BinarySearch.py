# # 재귀함수를 이용한 구현
# def binary_search(array,target,start,end):
#   if start>end:
#     return None

#   mid = (start+end) // 2
  
#   if array[mid] > target:
#     return binary_search(array,target,start,mid-1)
#   elif array[mid] < target: 
#     return binary_search(array,target,mid+1,end)
#   else: #array[mid] == target:
#     return mid
#   # return 유무에 따른 차이는 운동갔다와서 생각해보셈
#   # 처음에 return 안써줘서 찾는값이 없다고 떴음
#   # 그말은 result == None 즉 start>end 

# n,target = list(map(int,input().split()))
# array = list(map(int,input().split()))

# result = binary_search(array,target,0,n-1)

# if result == None:
#   print("찾는 값이 없습니다")
# else:
#   print(result+1)

# 반복문으로 구현한 이진탐색 
def binary_search(array,target,start,end):
  while start <= end:
    mid = (start+end) // 2
    if array[mid] == target:
      return mid
    elif array[mid] > target:
      end = mid-1
    elif array[mid] < target:
      start = mid+1

  return None

n, target = list(map(int,input().split()))
array = list(map(int,input().split()))

result = binary_search(array,target,0,n-1)

if result == None:
  print("찾는값이 없습니다")
else:
  print(result+1)

# import sys
# input_data = sys.stdin.readline().rstrip()
# print(input_data)

    