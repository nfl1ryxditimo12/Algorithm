# 리스트 컴프리헨션
# 2차원 배열을 손쉽게 초기화 할 수 있는 기능이다

# 0부터 19까지의 수 중에서 홀수만 포함하는 리스트
array1 = [i for i in range(20) if i % 2 == 1]

print(array1)

# 0으로 초기화 된 10x10 크기의 2차원 배열
array2 = [[0 for i in range(10)] for j in range(10)]

for i in range(10):
    for j in range(10):
        print(array2[i][j],end=' ')
    print()

print("=============================================")

'''
리스트 관련 메서드

list.append()               :   리스트에 원소 하나 삽입할때 사용한다 (리스트 맨 끝에 삽입)

list.sort()                 :   리스트를 오름차순으로 정렬한다
list.sort(reverse = True)   :   리스트를 내림차순으로 정렬한다

list.reverse()              :   리스트 순서를 모두 뒤바꾼다

list.insert()               :   insert(위치,값) 원하는 위치에 값을 삽입한다

list.count()                :   리스트의 특정한 값의 개수를 셀 때 사용한다

list.remove()               :   리스트의 특정한 값을 제거할 때 사용한다
'''

list=[1,4,7,2,6,5,3,6,7,0]

list.append(9)
print(list)

list.sort()
print(list)

list.sort(reverse=True)
print(list)

list.reverse()
print(list)

list.insert(11,10)
print(list)

list.count(4)
print(list.count(6))

list.remove(10)
print(list)