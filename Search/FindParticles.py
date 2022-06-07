# # 이진탐색
# def binary_search(array,target,start,end):
#   while start <= end:
#     mid = (start+end) // 2
#     if array[mid] == target:
#       return mid
#     elif array[mid] > target:
#       end = mid-1
#     else:
#       start = mid + 1
#   return None
#   # 여기 리턴은 반복문에 속한게 아님

# n = int(input())
# array = list(map(int,input().split()))
# array.sort()

# # 비교할 데이터 수 입력받기
# m = int(input())
# compare = list(map(int,input().split()))


# for i in compare:
#   result = binary_search(array,i,0,n-1)
#   if result != None:
#     print('yes', end = ' ')
#   else:
#     print('no', end = ' ')

# # 계수 정렬 이용
# n = int(input())
# array = [0] * 100001

# for i in input().split():
#   array[int(i)] =1

# m = int(input())
# compare = list(map(int,input().split()))

# for i in compare:
#   if array[i] == 1:
#     print('yes', end = ' ')
#   else:
#     print('no', end = ' ')

# 집합자료형 이용
n = int(input())
array = set(map(int,input().split()))

m = int(input())
x = list(map(int,input().split()))

for i in x:
  if i in array:
    print("yes", end = ' ')
  else:
    print("no", end = ' ')