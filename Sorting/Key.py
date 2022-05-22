array = [('바나나',2),('사과',5),('당근',3)]

# 데이터의 두번째 원소를 기준으로 함
def setting(data):
  return data[1] 

result = sorted(array,key = setting)
print(result)

