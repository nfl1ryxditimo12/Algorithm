# collections 라이브러리는 유용한 자료구조를 제공하는 표준 라이브러리다.

from collections import deque

data = deque([2,3,4])
data.appendleft(1)
data.append(5)

print(data)
print(list(data))

from collections import Counter

counter = Counter(['red','blue','red','green','blue','blue'])

print(counter['blue'])      # 'blue' 가 등장한 횟수 출력
print(counter['green'])     # 'green' 이 등장한 횟수 출력
print(counter['red'])       # 'red' 가 등장한 횟수 출력
print(dict(counter))        # 사전 자료형으로 변경