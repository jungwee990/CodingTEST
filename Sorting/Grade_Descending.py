n = int(input())

array = []
# 학생 이름과 성적을 튜플 형태로 입력받는다
# 키, 밸류값으로 이름과 성적을 한쌍으로 만들고 성적을 기준으로 정렬한다
for i in range(n):
  input_data = input().split() 
  array.append((input_data[0],int(input_data[1])))
  # input()의 기본값이 str을 받는건가? yes 심지어 숫자를 입력받아도 
  # str으로 취급하니 주의 해야함

array = sorted(array, key = lambda student:student[1])

for student in array:
  print(student[0], end = ' ')