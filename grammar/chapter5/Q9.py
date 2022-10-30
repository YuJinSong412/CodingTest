def add(a):
    result = 0
    for i in range(len(a)):
        result += a[i]
    print(result)

a = list(map(int,input().split()))
add(a)

