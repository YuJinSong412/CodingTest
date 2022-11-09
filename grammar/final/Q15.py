a = list(input().split())

for i in a:
    c = [0 for i in range(10)]
    for j in range(len(i)):
        x = int(i[j])
        c[x] += 1
    count = 0
    for k in c:
        if k != 1:
            print("false", end =" ")
            break
        else:
            count += 1
            if count == 10:
                print("true", end =" ")
