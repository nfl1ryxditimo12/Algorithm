print("***************************************************")
array = [3,5,1,2,4]
summary = 0

for x in array:
    summary += x

print(summary)

# x가 5번 더해져 summary 가 만들어졌으니 시간복잡도는 O(5)

print("***************************************************")
a = 5
b = 7
print(a+b)

# a+b 연산이 한번 이루어졌으니 시간 복잡도는 O(1)

print("***************************************************")

for i in array:
    for j in array:
        temp = i * j
        print(temp)

