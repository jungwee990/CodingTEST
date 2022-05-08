# def recursive_func(i):
#   if i == 100:
#     return

#   print(i, '번째 재귀 함수에서', i+1, '번째 재귀 함수를 호출합니다')
#   recursive_func(i+1)
#   print(i,'번째 재귀 함수를 종료합니다.')

# recursive_func(1)

# 반복적으로 구현
def iterative(n):
  result = 1
  for i in range(1,n+1):
    result *= i
  return result

def recursive(n):
  if n <= 1:
    return 1
  return n * recursive(n-1)

print('반복적으로 팩토리얼 구현', iterative(100))
print('재귀적으로 구현', recursive(100))

  
  
