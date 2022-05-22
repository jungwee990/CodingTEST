def Sequential_search(n,target,array):
  for i in range(n):
    if array[i] == target:
      return i+1

# 첫줄에 n과 찾을 이름을 입력받는다
print("n과 찾을 이름을 공백을 이용해 입력해주세요")
input_data = input().split()
n = int(input_data[0])
target = input_data[1]


print("이름을 n개 입력해주세요.(공백이용)")
array = input().split()
#split()함수는 스트링을 포함하는 list를 반환한다
print(Sequential_search(n,target,array))


