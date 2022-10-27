n = int(input())

array = [[] for _ in range(n)]
for i in range(n):
    data = input().split()
    array[i].append(data[0])
    array[i].append(int(data[1]))

array = sorted(array, key = lambda x:x[1])

for student in array:
    print(student[0], end=' ')

