# itertools 는 파이썬에서 반복되는 데이터를 처리하는 기능을 포함하고 있는 라이브러리이다.

data = ['A','B','C'] # 데이터 준비

# permutations 는 리스트와 같은 iterable 객체에서 r개의 데이터를 뽑아 일렬로 나열하는 모든 경우를 계산해준다

from itertools import permutations

result1 = list(permutations(data,3)) # 모든 순열 구하기
print(result1)

# combinations 는 리스트와 같은 객체에서 r개의 데이터를 뽑아 순서를 고려하지 않고 나열하는 모든 경우를 계산한다.

from itertools import combinations

result2 = list(combinations(data,2))
print(result2)

# product 는 permutations 와 같이 리스트와 같은 객체에서 r개의 데이터를 뽑아 일렬로 나열하는 모든 경우를 계산한다.

from itertools import product

result3 = list(product(data,repeat=2))
print(result3)

# combinations_with_replacement 는 combinations 와 같이 리스트와 같은 객체에서 r개의 데이터를 뽑아 순서를 고려하지 않고 나열하는 모든 경우를 계산한다.

from itertools import combinations_with_replacement

result4 = list(combinations_with_replacement(data,2))
print(result4)