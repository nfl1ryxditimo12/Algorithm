# 주요 라이브러리

# 파이썬은 여러가지 라이브러리를 제공하는데 알고리즘에 필요한 라이브러리는 6가지 정도이다

# 내장함수 : print(), input() 과 같은 기본 입출력 기능부터 sorted() 와 같은 정렬기능을 포함하고 있는 기본 내장 라이브러리이다.
# itertools : 반복되는 형태의 데이터를 처리하는 기능이다.
# heapq : 힙(Heap) 기능을 제공하는 라이브러리이다. 우선순위 큐 기능을 구현하기 위해 사용한다.
# bisect : 이진 탐색(Binary Search) 기능을 제공하는 라이브러리이다.
# collections : 덱(deque), 카운터(Counter) 등의 유용한 자료구조를 포함하고 있다.
# math : 필수적인 수학적 기능을 제공하는 라이브러리이다. 팩토리얼, 제곱근, 최대공약수, 삼각함수 관련 함수부터 파이와 같은 상수를 포함하고 있다.

# 내장함수

# 총합 구하는 함수 sum
result1 = sum([1, 2, 3, 4, 5])
print(result1)

# 최솟값 구하는 함수 min
result2 = min(7, 3, 5, 2)
print(result2)

# 최대값 구하는 함수 max
result3 = max(7, 3, 5, 2)
print(result3)

# 수학 수식이 문자열 형식으로 들어오면 계산한 결과를 반환하는 함수 eval
result4 = eval("(3+5)*7")
print(result4)
print(type(result4))

# 오름차순으로 정렬
result5 = sorted([9, 1, 8, 5, 4])
print(result5)

# 내림차순으로 정렬
result5 = sorted([9, 1, 8, 5, 4], reverse=True)
print(result5)

# 두번째 원소를 기준으로 내림차순 한다면 밑의 방식으로 사용할 수 있다.
result6 = sorted([('홍길동', 35), ('이순신', 75), ('아무개', 50)], key=lambda x: x[1], reverse=True)
print(result6)

# 리스트와 같은 객체는 기본적으로 sort() 함수를 내재하고 있어 굳이 sorted() 함수를 사용하지 않아도 된다
data = [9,1,8,5,4]
data.sort()
print(data)