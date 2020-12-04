# 입력

# 파이썬에서 데이터를 입력받을 때 대부분 input() 함수를 사용한다
# 하지만 여러 데이터를 받을땐 input().split() 뒤에 split 함수를 붙여줘야 한다

# map 함수와 list 함수를 활용해 한번에 정수형으로 변경하기
data1 = list(map(int,input().split()))
print(data1)

# 내림차순으로 학생 데이터 정렬
num = int(input()) # 학생 수
data2 = list(map(int,input().split())) # 학생 성적
data2.sort(reverse=True) # 리스트 내림차순 정렬

for i in range(len(data2)):
    print(data2[i],end=' ') # 공백을 기준으로 출력

# readline() 함수

# readline 함수는 엄청나게 많은 데이터를 받을 때 사용된다

import sys

data = sys.stdin.readline().rstrip()
print(data)
