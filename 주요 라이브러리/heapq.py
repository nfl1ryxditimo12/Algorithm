# heapq 는 최단 경로 알고리즘을 포함해 당양한 알고리즘에서 우선순위 큐 기능을 구현하고자 할 때 사용된다.

# 힙에 원소를 삽일할 때는 heapq.heappush() 메서드를 이용하고
# 힙에 원소를 꺼낼 때는 heapq.heappop() 메서드를 이용한다.

import heapq


def heapsort1(iterable):
    h = []
    result = []

    # 모든 원소를 차례대로 힙에 삽입
    for value in iterable:
        heapq.heappush(h, value)

    # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
    for i in range(len(h)):
        result.append(heapq.heappop(h))

    return result

result1 = heapsort1([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
print(result1)

# 파이썬에선 최대 힙을 제공하지 않는다. 따라서 heapq 라이브러리를 이용하여 최대 힙을 구현해야 할 때는
# 원소의 부호를 임시로 변경하는 방식을 사용한다.

def heapsort2(iterable):
    h = []
    result = []

    # 모든 원소를 차례대로 힙에 삽입
    for value in iterable:
        heapq.heappush(h, -value)

    # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
    for i in range(len(h)):
        result.append(-heapq.heappop(h))

    return result

result2 = heapsort2([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
print(result2)